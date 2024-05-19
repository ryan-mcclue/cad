#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement
def kmost(nums, k):
  hist_map = {}
  for i in nums:
    key = str(i)
    if key not in hist_map:
      hist_map[key] = 1
    else:
      hist_map[key] += 1

  # Could construct a max heap from histogram in O(n)
  # Then do a heap pop k times, k*logn; heapq.nlargest(k, hist_map, key=hist_map.get)
  # Heap pop involves swapping root with last element and then removing.
  # If root is less than both its children, sift down, i.e. swap it with the largest of its two children and recurse

  # use list comprehension to ensure not duplicate memory references
  ksort = [[0, 0] for _ in range(k)]
  for num,freq in hist_map.items():
    for i in range(k):
      if freq > ksort[i][1]:
        if i == k - 1:
          ksort[i][0] = num
          ksort[i][1] = freq
        else:
          for j in range(k - 1, i, -1):
            ksort[j][0] = ksort[j - 1][0]
            ksort[j][1] = ksort[j - 1][1]
          ksort[i][0] = num
          ksort[i][1] = freq
        break

  print(ksort)

kmost([10, 20, 20, 10, 30, 40], 3)
