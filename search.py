#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement
def duplicate(nums):
  d = []
  # we are mutating array to negative to indicate it has been seen
  for n in nums:
    v = abs(n)
    if nums[v] < 0:
      d.append(n)
    else:
      nums[v] = nums[v] * -1
  return d

def packed_search(colors_lane, search):
  assert search < 0x4, "search only 2bit color"
  search_dup = search | (search << 2) | (search << 4) | (search << 6)

  eq_straddle = ~(colors_lane ^ search) 
  straddle_mask = 0b10101010
  eq = eq & ((eq_straddle & straddle_mask) >> 1)
  return eq

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


def arr2bst(a, temp):
  a_len = len(a)
  if a_len == 0:
    return None
  elif a_len == 1:
    return Node(a[0])
  else:
    mid = a_len // 2
    n = Node(a[mid])
    if a_len == 2:
      n.left = Node(a[0])
    else:
      half0 = a[0:mid]
      half1 = a[mid+1:]
      n.left = arr2bst(half0)
      n.right = arr2bst(half1)
    return n

def search_bst():
  pass

# half0_i = 0
# half1_i = 0
# for i in range(a_len):
#   if half0[half0_i] == half1[half1_i]:
#     out.append(half1[half1_i])
#     half1_i += 1
#   elif half0[half0_i] < half1[half1_i]:
#     out.append(half0[half0_i])
#     half0_i += 1
#  COPYBACK REQUIRED:
#for i in range(count):
#  orig[i] = temp[i]
