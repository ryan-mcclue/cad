#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def rotate_copy(a):
  a_w = len(a[0])
  a_h = len(a)
  b_h = a_w
  b_w = a_h
  b = [[0] * b_w for i in range(b_h)]

  # first row becomes last column
  for y in range(a_h):
    for x in range(a_w):
      b[x][b_w - y - 1] = a[y][x]


  print(b)

rotate_copy([[1,2],[3,4],[5,6]])
