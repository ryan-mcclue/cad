#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# items selected are rows: (value, weight)
# columns are resulting capacity


subproblem:
opt(i, k) where maximum value using up to 'i' units of weight using only 'k' items
recurrence relation:
opt(i, k) = max(opt(i - w, k - 1) + v)
def k(items, cap):
  dp = int[len(cap)+1][capacity+1]


