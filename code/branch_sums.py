#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def branch_sums(root):
  sums = []
  calculate_branch_sums(root, 0, sums)

  return sums

def calculate_branch_sums(node, cumulative_sum, sums):
  if node is None:
    return

  cumulative_sum += node.value
  if node.left == None and node.right == None:
    sums.append(cumulative_sum)

  calculate_branch_sums(node.left, cumulative_sum, sums)
  calculate_branch_sums(node.right, cumulative_sum, sums)
