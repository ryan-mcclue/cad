#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# 1. Thinking + scaffolding
# What I'm thinking is to use a trie data structure
# Each node will have additional metadata that marks it as end-of-word
# To find root, will have O(n) respect to input
# Then to search all others in DFS, will be O(n), but optimal as all searches in result set
# How does that sound?
class Node:
  def __init__(self):
    self.children = {}
    self.is_word = False

class Trie:
  def __init__(self):
    self.root = Node()

  # IMPORTANT: single node for repeated letter
  def add_word(self, word):
    cur_node = self.root
    for c in word:
      if c in cur_node.children:
        cur_node = cur_node.children[c]
      else:
        new_node = Node()
        cur_node.children[c] = new_node
        cur_node = new_node
    cur_node.is_word = True

  def find_words(self, prefix):
    # first find root to do dfs from
    cur_node = self.root
    for c in prefix:
      if c not in cur_node.children:
        return []
      else:
        cur_node = cur_node.children[c]

    lst = []
    self._find_words(prefix, cur_node, lst)
    return lst

  def _find_words(self, prefix, node, lst):
    if node.is_word:
      lst.append(prefix)
    for c in node.children:
      self._find_words(prefix + c, node.children[c], lst)

t = Trie()
t.add_word("ryan") 
t.add_word("graham") 
t.add_word("reginald") 
t.add_word("rygel") 
print(t.find_words("ry"))


# 2. Coding
# if many more elements might encounter stack overflow, so iterative

# 3. Questions for them
#  - what do you think is unique aboout this company that you like about it
#  - how are the engineer teams composed of? is there an electrical engineer, data scientist etc?
#  - what is a typical day? how do you engineers work in teams?
#  - what are the biggest challenges engineers are facing at the moment? is it shipping new features or maintaining code?
