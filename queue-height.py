#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def q(q):
  height_sort = sorted(q, key=lambda x: (-x[0], x[1]))  
  
  o = []
  for p in height_sort:
    o.insert(p[1], p)

  return o

print(q([[1,2], [2,2]]))
