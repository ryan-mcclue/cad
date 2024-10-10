#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement


def parse_facts(facts):
  return {}

facts = {
  'in': {'m': 2.34},
  'm': []
}

def convert(query):
  base, unit, to_unit = query

  unit_node = facts.get(unit, '')
  assert unit_node, "not registered"

  to_unit_node = unit_node.get(to_unit, '')
  assert unit_node, "not convertable"
  
  result = base * to_unit_node


