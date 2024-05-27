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

  # binary logic puzzle?
  # bit level puzzles in hackers delight
  # XOR is !=, so XOR NOT is ==, ~(val ^ replicated)

