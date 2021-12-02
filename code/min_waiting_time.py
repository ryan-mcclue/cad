#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement


def min_waiting_time(queries):
  if len(queries) == 1:
    return 0 
  if len(queries) == 2:
    return min(queries)

  sorted_list = sorted(queries)
  num_entries = len(sorted_list)

  total_waiting_time = 0
  for (index, elem) in enumerate(sorted_list):
    total_waiting_time += (elem * (num_entries - index - 1))

  return total_waiting_time
