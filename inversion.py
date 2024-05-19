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

def generate_tree_iterative(level):
#  current = r
#  while current != None or len(stack) == 0:
#    push(current)
#    current = current.l
#    if current != None:
#      continue
#    current = pop()
#    print(current)
#    current = current.right
  return r

# inorder
def dump_node(n, level, indent_str, out):
  if n is not None:
    dump_node(n.l, level+1, indent_str, out)
    for i in range(level):
      out.append(indent_str)
    out.append(f"{n.v}\n")
    dump_node(n.r, level+1, indent_str, out)

#def preorder(r):
#  if r == None:
#    return
#  push(r)
#  while len(stack) != 0:
#    n = stack.pop()
#    print(n.v)
#    push(n.r) # as want reverse
#    push(n.l)
#
## just store preorder in another stack and empty that to reverse it
#def postorder(r):
#  pass
#
#def inorder(r):
#  current = r
#  while current != None or len(stack) == 0:
#    push(current)
#    current = current.l
#    if current != None:
#      continue
#    current = pop()
#    print(current)
#    current = current.right

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
  r = None
  with Timer("gen_tree"):
    r = generate_tree(3)

  out = []
  dump_node(r, 0, "  ", out)
  s = "".join(out)
  print(s)

  a = generate_tree_iterative(3)
  out = []
  dump_node(a, 0, "  ", out)
  s = "".join(out)
  print(s)

  #i = create_inverted_tree(r)
  #out = []
  #dump_node(i, 0, "  ", out)
  #s = "".join(out)
  #print(s)

  return

if __name__ == "__main__":
  # NOTE(Ryan): Disable breakpoints if not running under a debugger
  if sys.gettrace() is None:
    os.environ["PYTHONBREAKPOINT"] = "0"

  directory_of_running_script = pathlib.Path(__file__).parent.resolve()
  os.chdir(directory_of_running_script)

  main()
