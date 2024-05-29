#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# Could do a state machine

def m(a):
  if len(a) < 3:
    return False

  are_increasing = True
  for i in range(len(a)):
    c = a[i]
    
    if are_increasing:
      if i + 1 == len(a):
        return False
      else:
        n = a[i + 1]
        if n <= c:
          are_increasing = False
    else:
      p = a[i - 1]
      if p <= c:
        return False

  return True
    

print(m([2, 1]))
print(m([3, 5, 5]))
