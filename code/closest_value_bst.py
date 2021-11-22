#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

class Node:
  def __init__(self, val, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

def solution(bst, target):
  cur_node = bst
  closest = cur_node.value

  while cur_node is not None:
    if abs(target - cur_node.value) < abs(target - closest):
      closest = cur_node.value

    if target < cur_node.value:
      cur_node = cur_node.left
    elif target > cur_node.value:
      cur_node = cur_node.right
    else:
      break

  return closest
