#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import code.two_number_sum as two_number_sum

import itertools

def test_pair():
  assert two_number_sum.solution_quadratic((1, -22, 3, 4, 5), 8) in \
           itertools.permutations((3, 5), 2)
  assert two_number_sum.solution_linear((1, 2, 3, 4, 5), 8) in \
           itertools.permutations((3, 5), 2)

def test_no_pairs():
  assert two_number_sum.solution_quadratic((1, 2, 3, 4, 5), 10) == ()
  assert two_number_sum.solution_linear((1, 2, -3, 4, 5), 10) == ()
