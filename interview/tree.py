#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# 1. Thinking + scaffolding
# What I'm thinking is to use a trie data structure
# Each node will have additional metadata that marks it as end-of-word
# To find root, will have O(n) respect to input
# Then to search all others in DFS, will be O(n), but optimal as all searches in result set
# I've heard of union-find, but I'd have to look it up.
# Is it ok to do naive version first?
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

# t = Trie()
# t.add_word("ryan") 
# t.add_word("graham") 
# t.add_word("reginald") 
# t.add_word("rygel") 
# print(t.find_words("ry"))

class TrieNode:
  def __init__(self, val):
    self.val = val
    self.children = []
    self.full_word = False

class TrieTree:
  def __init__(self):
    self.root = TrieNode('')

  def add_word(self, word):
    n = self.root

    for c in word:
      if c == n.val:
        continue
      else:
        child_found = False
        for child in n.children:
          if c == child.val:
            n = child
            child_found  = True
            break
        if not child_found:
          new_node = TrieNode(c)
          n.children.append(new_node)
          n = new_node
    n.full_word = True

  def _print_trie(self, node, level):
    num_children = len(node.children)
    half = num_children // 2
    for i in range(half):
      self._print_trie(node.children[i], level + 1)
    print(f"{' ' * level}{node.val}\n")
    for i in range(half, num_children):
      self._print_trie(node.children[i], level + 1)

  def print_trie(self):
    self._print_trie(self.root, 0)

  def dfs(self, node, prefix, words):
    for child in node.children:
      new_prefix = prefix + child.val
      if child.full_word:
        words.append(new_prefix)
      else:
        self.dfs(child, new_prefix, words)

  def find_words(self, prefix):
    n = self.root
    for c in prefix:
      if c == n.val:
        continue 
      else:
        for child in n.children:
          if c == child.val:
            n = child
            break

    words = []
    if n.full_word:
      words.append(prefix)

    self.dfs(n, prefix, words)
    print(words)

if __name__ == "__main__":
  trie = TrieTree() 
  trie.add_word("walter")
  trie.add_word("william")
  trie.add_word("wilhielm")
  trie.add_word("wigan")
  # trie.print_trie()
  trie.find_words("w")

# 2. Coding
# if many more elements might encounter stack overflow, so iterative
# must remember to loop over repeated letters; can imagine having a bug there 

# 3. Questions for them
#  - what do you think is unique aboout this company that you like about it
#  - how are the engineer teams composed of? is there an electrical engineer, data scientist etc?
#  - what is a typical day? how do you engineers work in teams?
#  - what are the biggest challenges engineers are facing at the moment? is it shipping new features or maintaining code?
