#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# could do hash map hist.

# in-place sort with left/right pointers
def s(a):
  i = 0
  index1 = 0
  index3 = len(a) - 1
  while i <= index3:
    if a[i] == 1:
      swap(i, index1)
      index1 += 1
      i += 1
    elif a[i] == 2:
      i += 1
    elif a[i] == 3:
      swap(i, index3)
      index3 -= 1
