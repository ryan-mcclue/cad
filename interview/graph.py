
class Node:
    def __init__(self, unit):
        self.unit = unit
        self.connections = {}  # {connected_node: conversion_factor}

    def add_connection(self, other_node, factor):
        self.connections[other_node] = factor
        other_node.connections[self] = 1 / factor

class ConversionGraph:
    def __init__(self):
        self.nodes = {}

    def add_unit(self, unit):
        if unit not in self.nodes:
            self.nodes[unit] = Node(unit)

    def add_conversion(self, from_unit, to_unit, factor):
        self.add_unit(from_unit)
        self.add_unit(to_unit)
        self.nodes[from_unit].add_connection(self.nodes[to_unit], factor)

    def find_conversion_path(self, from_unit, to_unit):
        start = self.nodes[from_unit]
        end = self.nodes[to_unit]
        
        queue = [(start, [start], 1)]
        visited = set()

        while queue:
            (node, path, factor) = queue.pop(0)
            if node not in visited:
                visited.add(node)
                
                if node == end:
                    return path, factor
                
                for next_node, edge_factor in node.connections.items():
                    if next_node not in visited:
                        new_path = path + [next_node]
                        new_factor = factor * edge_factor
                        queue.append((next_node, new_path, new_factor))
        
        return None, None

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        path, factor = self.find_conversion_path(from_unit, to_unit)
        if path is None:
            return "not convertible"

        return round(value * factor, 3)

def parse_input(query):
    parts = query.split('=')
    left = parts[0].strip().split()
    right = parts[1].strip().split()
    
    value = float(left[0])
    from_unit = left[1]
    to_unit = right[1]
    
    return value, from_unit, to_unit

# Create and populate the conversion graph
graph = ConversionGraph()
graph.add_conversion('m', 'ft', 3.28084)
graph.add_conversion('ft', 'in', 12)
graph.add_conversion('hr', 'min', 60)
graph.add_conversion('min', 'sec', 60)

# Main program
while True:
    query = input("Enter conversion query (or 'q' to quit): ")
    if query.lower() == 'q':
        break
    
    try:
        value, from_unit, to_unit = parse_input(query)
        result = graph.convert(value, from_unit, to_unit)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
