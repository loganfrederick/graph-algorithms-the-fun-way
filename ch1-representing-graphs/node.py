from edge import Edge

class Node:
	def __init__(self, index, label=None):
		self.index = index
		self.edges = {}
		self.label = label # Optional to identify the node or mark its current state
		
	def num_edges(self):
		return len(self.edges)
		
	def get_edge(self, neighbor):
		if neighbor in self.edges:
			return self.edges[neighbor]
		return None	
	
	def add_edge(self, neighbor, weight):
		self.edges[neighbor] = Edge(self.index, neighbor, weight)
	
	def remove_edge(self, neighbor):
		if neighbor in self.edges:
			del self.edges[neighbor]
			
	def get_edge_list(self):
		# Returns edges in their dictionary ordering
		return list(self.edges.values())
		
	def get_sorted_Edge_list(self):
		# Returns edges in order of increasing neighbor index
		result = []
		neighbors = (list)(self.edges.keys())
		neighbors.sort()
		
		for n in neighbors:
			result.append(self.edges[n])
		return result