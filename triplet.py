#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def t(nums):
  h = {}
  
  for a in nums:
    for b in nums:
      s = a*a + b*b
      if s in h:
        triplets.append(a,b,sqrt(s))
