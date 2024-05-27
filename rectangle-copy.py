#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def c():
  a_start = pitch_a * a_min_y + a_min_x
  b_start = pitch_b * b_min_y + b_min_x

  for y in range(a_min_y, a_max_y):
    for x in range(a_min_x, a_max_x):
      b_start[x] = a_start[x]
    a_start += a_pitch
    b_start += b_pitch

  # b[y_i][x_i] = a[y_i][x_i]
