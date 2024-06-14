#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement
def r(first):
  cur = first
  prev = None
  while cur != None:
    cur_next = cur.next
    cur.next = prev
    prev = cur
    cur = cur_next
  return prev
