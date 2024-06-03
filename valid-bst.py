#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def v(n, low=100000, high=-100000):
  if n == None:
    return True
  
  return n.v < low and n.v > high and v(n.l, n.v, high) and v(n.r, low, n.v)
