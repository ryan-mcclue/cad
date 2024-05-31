#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# recursive divide and conquer on an array
# (in C, would pass in count)
def arr2bst(a):
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
