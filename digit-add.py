#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def pow2(n):
  return (n & (n - 1)) == 0

def least_significant_digit(n):
  return (n % 10)

def max(a, b):
  return (a + b + abs(a - b)) // 2
def min(a, b):
  return (a + b - abs(a - b)) // 2

# >> arithmetic shift


def digit_add(n):
  digit_sum = 0
  cur_num = n
  found_1digit = False
  # number of digits = floor(log10(num)) + 1
  while not found_1digit:
    while cur_num > 0:
      d = cur_num % 10
      cur_num = cur_num // 10
      digit_sum += d

    if digit_sum <= 9:
      found_1digit = True
    else:
      cur_num = digit_sum
      digit_sum = 0
      
  return digit_sum

print(digit_add(38))
