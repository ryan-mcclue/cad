#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement
ObjectOrientation:
class Solution:
  def dfs(n):
   ret = []
   dfs_helper(n, ret)
   return ''.join(ret)
  def dfs_helper(n, ret):
    ret.append(n) 
print(Solution().dfs(n))

would also have public and private methods etc.
interface Animal {
  public bool eat(item);
}
class Dog implements Animal {
  public bool eat(item) { return item == 'meat'; }
}
class Cafe:
  public feed(Animal a) {
    a.eat('meat')
  }
}

def reverse(s):
  if len(s) == 0:
    return ""
  else:
    return reverse(s[1:]) + s[0]
max. connected components in grid.
autocomplete
