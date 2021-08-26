#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import pytest

import src.valid_bst as valid_bst

def test_example():
  root = valid_bst.Node(10)
  root.left = valid_bst.Node(1)
  root.right = valid_bst.Node(5)
