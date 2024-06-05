#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def s(letters, word):
  h = [0] * 256
  for l in letters:
    h[l] += 1
  for l in word:
    if h[l] > 0:
      h[l] -= 1
    else:
      return False
  return True

def ll_add(l1, l2):
  # for recursive, just return next Node
  c = 0
  n1 = l1
  n2 = l2
  l3 = None
  while True:
    v1 = 0
    if n1 != None:
      v1 = n1.v
      n1 = n1.next
    v2 = 0
    if n2 != None:
      v2 = n2.v
      n2 = n2.next
    s = v1 + v2 + c
    if s >= 10:
      c = 1
      s = s % 10
    
    n3 = Node(None, s)
    push(l3, n3)

    if n1 == None and n2 == None:
      if c > 0:
        n3 = Node(None, c)
        push(l3, n3)
      break
  return l3
