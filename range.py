#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# space complexity for recursive is recursion depth
def bin_search(a, v, find_first):
  low = 0
  high = len(a) - 1
  while True:
    mid = (low + (high - low)) // 2
    if high < low:
      return -1
    if find_first:
      if a[mid] == v and (mid == 0 or a[mid-1] < v):
        return mid
      elif a[mid] < v:
        low = mid + 1
      else:
        high = mid - 1
    else:
      if a[mid] == v and (mid == len(a) - 1 or a[mid+1] > v):
        return mid
      elif a[mid] > v:
        high = mid - 1
      else:
        low = mid + 1



