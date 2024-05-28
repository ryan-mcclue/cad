#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def l_rec(n, leaves):
  if n == None:
    return
  elif n.l == None and n.r == None:
    leaves.append(n.v)
  else:
    l(n.l, leaves)
    l(n.r, leaves)

def l_it(r):
  leaves = []
  s = []
  s.push(r)
  while len(s) > 0:
    n = s.pop()
    if n == None:
      continue
    elif n.l == None and n.r == None:
      leaves.append(n)
    else:
      s.push(n.r)
      s.push(n.l)
  return leaves
