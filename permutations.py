#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement
def p(a):
  remaining = a
  res = []
  cur = []
  generate_permutations(cur, remaining, res)
  return res

# n! lists complexity
def generate_permutations(cur, remaining, res):
  if len(remaining) == 0:
    res.append(cur)
  else:
    for num in remaining:
      next_cur = cur.copy()
      next_cur.append(num)
      next_remaining = remaining.copy()
      next_remaining.remove(num)
      generate_permutations(next_cur, next_remaining, res)

print(p([1,2,3]))
