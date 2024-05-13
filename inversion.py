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

def generate_tree(level=3):
  if level == 0:
    return None
  else:
    # preorder
    n = Node(level)
    n.l = generate_tree(level - 1)
    n.r = generate_tree(level - 1)
    return n

# inorder
def print_tree(n, indent=0, indent_str="  "):
  if n is not None:
    print_tree(n.l, indent + 1)
    for i in range(indent):
      print(indent_str, end="")
    print(f"{n.v}")
    print_tree(n.r, indent + 1)
    

def main():
  r = None
  with Timer("gen_tree"):
    r = generate_tree()

  print_tree(r)

  return

if __name__ == "__main__":
  # NOTE(Ryan): Disable breakpoints if not running under a debugger
  if sys.gettrace() is None:
    os.environ["PYTHONBREAKPOINT"] = "0"

  directory_of_running_script = pathlib.Path(__file__).parent.resolve()
  os.chdir(directory_of_running_script)

  main()
