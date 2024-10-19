#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# https://coderpad.io/

class Reader:
  def __init__(self):
    self.users = []
    

class User:
  def __init__(self):
    self.library = [] # use list here as ordered and simple
    # assume library would be under 200 elements
    # assume access pattern want ordered

    self.active_book = 0 
    self.last_page = 0 # off-by-one error possible

  def add_book_to_library(self, b):
    # if want to check for duplicates, then id
    pass

  def remove_book_from_library(self, b):
    pass
    
class Book:
  def __init__(self):
    self.content = []
  
