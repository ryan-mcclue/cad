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
#print(perfect_number(28))

# could construct a max heap from histogram in O(n)
# then do a heap pop k times, k*logn
def kmost(nums, k):
  hist_map = {}
  for i in nums:
    key = str(i)
    if key not in hist_map:
      hist_map[key] = 1
    else:
      hist_map[key] += 1

  ksort = [[0, 0]] * k
  for num,freq in hist_map.items():
    for i in range(k):
      if freq > ksort[i][1]:
        if i == k - 1:
          print(f'setting {num}')
          ksort[i][0] = num
          ksort[i][1] = freq
        else:
          for j in range(k - 1, i, -1):
            ksort[j][0] = ksort[j - 1][0]
            ksort[j][1] = ksort[j - 1][1]
          print(f'setting {num}')
          ksort[i][0] = num
          ksort[i][1] = freq
        break

  print(ksort)

kmost([10, 20, 10, 30, 40], 2)
