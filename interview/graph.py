#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

# TODO: has_cycle function

GRAPH_DIM = 16
graph = [[0] * GRAPH_DIM] * GRAPH_DIM

units = {}
def unit_to_graph_i(unit):
  if unit in units:
    return units[unit]
  else
    units[unit] = len(units)

def parse_island_array(a):
  for y in range(len(a)):
    for x in range(len(a[0])):
      # ignore cycles
      if y == x:
        continue

      if a[y][x] == 1:
        # check left neighbour
        if a[y][x-1] == 1:
          graph[y][x-1] = 1
          graph[x-1][y - 1] = 1
        # check right neighbour
        if a[y][x+1] == 1:
          graph[y][x+1] = 1
          graph[x+1][y - 1] = 1
def set_connection(x, y):
  # mark as border
  if x == 0:
    graph[y][x] = -1

def find_islands():
  if graph[y][x] == 0:



def parse_facts(facts):
  for f in facts:
    src_amt, src_unit, dst_amt, dst_unit = f
    
    src_i = unit_to_graph_i(src_unit)
    dst_i = unit_to_graph_i(dst_unit)

    graph[src_i][dst_i] = src_amt / dst_amt
    graph[dst_i][src_i] = dst_amt / src_amt

def convert(query):
  amt, unit, to_unit = query
  assert unit in units, "unit not in knowledge base" 
  assert to_unit in units, "to_unit not in knowledge base" 

  start_i = unit_to_graph_i(unit)
  end_i = unit_to_graph_i(to_unit)
  visited[start_i] = True
  conversion = []
  dfs(start_i, conversion)

def dfs(start_i, conversion):
  if start_i == end_i:
    return

  for i in range(len(GRAPH_DIM)):
    conversion = graph[start_i][i]
    if conversion != 0 and not visited[i]:
      conversion[0] *= conversion
      visited[i] = True
      dfs(i, conversion)
      visited[i] = False
