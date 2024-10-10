#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import pathlib
import os
import sys
import time

from dataclasses import dataclass

@dataclass
class Node:
  v: int = 0
  l: 'Node' = None
  r: 'Node' = None

class Timer:
  def __init__(self, name):
    self.name = name
  def __enter__(self):
    self.start = time.time_ns()
  def __exit__(self, exception_type, exception_value, traceback):
    end = time.time_ns()
    print(f"{self.name}: {end - self.start}")

def generate_tree(level=4, counter=[0]):
  if level == 0:
    return None
  else:
    # preorder
    n = Node(level)
    n.v = counter[0]
    counter[0] += 1
    n.l = generate_tree(level - 1)
    n.r = generate_tree(level - 1)
    return n

# inorder
def dump_node(n, level, indent_str, out):
  if n is not None:
    dump_node(n.l, level+1, indent_str, out)
    for i in range(level):
      out.append(indent_str)
    out.append(f"{n.v}\n")
    dump_node(n.r, level+1, indent_str, out)

# bfs
def generate_tree_iterative(max_depth):
  c = 0
  num_nodes = 2 ** max_depth - 1
  nodes = []
  for i in range(num_nodes):
    n = Node()
    n.v = c
    c += 1
    nodes.append(n)

  for i in range(num_nodes):
    li = 2 * i + 1
    if li > num_nodes - 2: 
      break
    nodes[i].l = nodes[li]
    nodes[i].r = nodes[2 * i + 2]

  return nodes[0]

from queue import Queue

def bfs(n):
  nodes = Queue()
  nodes.put(n)

  while not nodes.empty():
    n = nodes.get() 
    if (n == None):
      continue
    print(n.v)
    nodes.put(n.l)
    nodes.put(n.r)

r = generate_tree_iterative(4)
bfs(r)

s = []
dump_node(r, 0, " ", s)
print("".join(s))


#def preorder(r):
#  if r == None:
#    return
#  push(r)
#  while len(stack) != 0:
#    n = stack.pop()
#    print(n.v)
#    push(n.r) # as want reverse
#    push(n.l)

#def inorder():
#  current = r
#  while current != None or len(stack) != 0:
#    while current != None:
#      push(current)
#      current = current.l
#    current = pop()
#    print(current)
#    current = current.right

## just store preorder in another stack and empty that to reverse it
#def postorder(r):
#  pass

def create_inverted_tree(n):
  if n == None:
    return None
  else:
    nn = Node()
    nn.v = n.v
    nn.l = create_inverted_tree(n.r)
    nn.r = create_inverted_tree(n.l)
    return nn

def main():
#  r = None
#
#  with Timer("gen_tree"):
#    r = generate_tree(3)
#
#  out = []
#  dump_node(r, 0, "  ", out)
#  s = "".join(out)
#  print(s)
#
#  a = gen_tree_preoder_it(3)
#  out = []
#  dump_node(a, 0, "  ", out)
#  s = "".join(out)
#  print(s)
#
#  #i = create_inverted_tree(r)
#  #out = []
#  #dump_node(i, 0, "  ", out)
#  #s = "".join(out)
#  #print(s)

  return

if __name__ == "__main__":
  # NOTE(Ryan): Disable breakpoints if not running under a debugger
  if sys.gettrace() is None:
    os.environ["PYTHONBREAKPOINT"] = "0"

  directory_of_running_script = pathlib.Path(__file__).parent.resolve()
  os.chdir(directory_of_running_script)

  main()
