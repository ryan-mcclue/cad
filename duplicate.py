#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def d(nums):
  d = []
  # we are mutating array to negative to indicate it has been seen
  for n in nums:
    v = abs(n)
    if nums[v] < 0:
      d.append(n)
    else:
      nums[v] = nums[v] * -1
  return d

h = [0] * len(nums)
for i in nums:
  h[i] += 1
