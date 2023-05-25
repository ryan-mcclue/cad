#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import pathlib
import os
import sys
import subprocess
import logging

from dataclasses import dataclass

def fatal_error(msg):
  logging.critical(msg)
  breakpoint()
  sys.exit()

def sort_bottom_up(lst):
  if isinstance(lst, list):
    for i in range(len(lst)):
      lst[i] = sort_bottom_up(lst[i])
    return sorted(lst)
  else:
    return lst

def any_order(lst1, lst2):
  return sort_bottom_up(lst1) == sort_bottom_up(lst2)

def two_number_sum_quadratic(array, target_sum):
  result = []

  for i in array:
    for j in array[i:]:
      if i + j == target_sum:
        result.append([i, j])

  return result

def two_number_sum_loglinear(array, target_sum):
  result = []

  sorted_array = sorted(array)

  left_i = 0
  right_i = len(sorted_array) - 1
  while left_i != right_i:
    left_val = sorted_array[left_i]
    right_val = sorted_array[right_i]

    test_sum = left_val + right_val

    if test_sum == target_sum:
      result.append([left_val, right_val])
      right_i -= 1
    elif test_sum > target_sum:
      right_i -= 1
    else:
      left_i += 1
  
  return result

def two_number_sum_linear(array, target_sum):
  result = []

  hash_map = {} 
  for i in array:
    hash_map[str(i)] = i

  for i in array:
    required_val = target_sum - i
    if required_val >= i:
      continue
    if hash_map.get(str(required_val)) is not None:
      result.append([i, required_val])

  return result


def test_two_number_sum():
  assert(any_order(two_number_sum_quadratic([1, 2, 3, 4, 5], 6), [[1, 5], [2, 4]]))
  assert(any_order(two_number_sum_loglinear([1, 2, 3, 4, 5], 6), [[1, 5], [2, 4]]))
  assert(any_order(two_number_sum_linear([1, 2, 3, 4, 5], 6), [[1, 5], [2, 4]]))


if __name__ == "__main__":
  # NOTE(Ryan): Disable breakpoints if not running under a debugger
  if sys.gettrace() is None:
    os.environ["PYTHONBREAKPOINT"] = "0"

  directory_of_running_script = pathlib.Path(__file__).parent.resolve()
  os.chdir(directory_of_running_script)

  test_two_number_sum()
