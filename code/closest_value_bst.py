#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

class Node:
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

def solution(bst, target):
  cur_node = bst
  prev_val, cur_val = 0, 0
  while True:
    cur_val = cur_node.val

    if target == cur_val:
      return cur_val

    if target > current_val:
      cur_node = cur_node.right

    if target < current_val:
      cur_node = cur_node.left

    if not cur_node:
      return current_val
