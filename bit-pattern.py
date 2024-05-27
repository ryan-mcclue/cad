#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# Optimal code generation uses patterns that the compiler can easily recognise
# Not necessarily the fewest instructions
# for (u32 i = 0; dst[i] = src[i]; i += 1)


def f(p, c):
  # OR together boolean ops to prevent ifs
  return (p & 3 == c) |
         (p >> 2 & 3 == c) |
         (p >> 4 & 3 == c) |
         (p >> 6 & 3 == c);

  # XOR is !=, so XOR NOT is ==, ~(val ^ replicated)
  any_two = 0b10110101 
  top1_set = any_two & 0b10101010
  any_two_set = any_two & (top1_set >> 1)
