#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def solution_quadratic(distinct_arr, target_sum):
  for lhs in distinct_arr:
    for rhs in distinct_arr:
      if lhs == rhs:
        continue
      if lhs + rhs == target_sum:
        return (lhs, rhs)
  return ()

def solution_linear(distinct_arr, target_sum):
  hashmap_arr = {} 
  for (index, value) in enumerate(distinct_arr):
    hashmap_arr[str(value)] = index

  for lhs in distinct_arr:
    required_rhs = target_sum - lhs
    if required_rhs != lhs and str(required_rhs) in hashmap_arr:
      return (lhs, required_rhs)

  return ()
