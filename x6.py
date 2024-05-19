#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement
def perfect_number(n):
  # hueristics for larger numbers prime determination?
  n = max(n, 0)
  divisor_sum = 0
  for i in range(1, n // 2 + 1, 1):
    if n % i == 0:
      divisor_sum += i
      # pair: n / i
    
  return divisor_sum == n

# if next factor equals prev factor pair, gone far enough
# n ** 0.5
# pair_sum = reduce(lambda x, y: x + y, num)
print(perfect_number(28))
