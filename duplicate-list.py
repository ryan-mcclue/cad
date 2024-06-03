#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def duplicate(first):
  prev_n = first
  cur_n = first.next
  delete_first = (prev_n.v == cur_n.v)
  while cur_n != None:
    delete_first = False
    while cur_n.v == cur_n.next.v:
      delete_first = True
      cur_n.next = cur_n.next.next
    if delete_first:
      prev_n.next = cur_n.next
    cur_n = cur_n.next
    prev_n = cur_n

  if delete_first:
    first = first.next
