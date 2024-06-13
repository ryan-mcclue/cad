#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def d(a):
  v = 0
  # double duplicates will knock each other out
  for n in a:
    v ^= n
  return v

print(d([4, 3, 2, 4, 199, 3, 2]))
