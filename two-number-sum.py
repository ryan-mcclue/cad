#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

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
