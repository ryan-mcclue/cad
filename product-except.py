#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def pe(nums):
  l_a = [0] * len(nums)
  l_p = 1
  for i in range(len(nums)):
    l_p *= nums[i]
    l_a[i] = l_p
  r_a = []
  r_p = 1
  for i in range(len(nums) - 1), -1, -1):
    r_p *= nums[i]
    r_p[i] = r_p

  o = []
  for i in range(len(o)):
    if i == 0:
      o[i] = r_a[1]
    elif i == len(o) - 1:
      o[i] = l_a[i - 1]
    else:
      o[i] = l_a[i - 1] * r_a[i + 1]

  return o
