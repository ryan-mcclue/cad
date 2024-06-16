#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# store other list that has maximum at that time
# if random insertion/deletion have heap
def push(s, v):
  s.stack.append(v)
  if s.maxes == None:
    s.maxes[0] = v
  else:
    new_max = s.maxes[-1]
    if v > new_max:
      new_max = v
    s.maxes.append(new_max)

def pop(s):
  s.stack.remove()
  s.maxes.remove()

def max(s):
  return s.maxes[-1]
