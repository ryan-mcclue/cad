#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

def get_dom(doms, i):
  if i < 0 || i >= len(doms):
    return NULL

def d(doms, forces):
  for f in forces:
    doms[f[0]] = f[1]

  change_made = True
  while change_made:
    change_made = False
    for i in range(len(doms)):
      one_ldom = get_dom(i - 1)
      two_ldom = get_dom(i - 2)
      one_rdom = get_dom(i + 1) 
      two_rdom = get_dom(i + 2) 
      cur_dom = get_dom(i)

      if cur_dom == RIGHT and one_rdom == UP and two_rdom != LEFT:
        doms[i + 1] = RIGHT
        change_made = True
      elif cur_dom == LEFT and one_ldom == UP and two_ldom != RIGHT: 
        doms[i - 1] = LEFT
        change_made = True
