
# from itertools import cycle

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for p in cycle(alphabet):
#   if p == 'z':
#   	break
#   else:
#   	print p

	
class Vertex:
	location = {}
	open = False
	
	def left(self):
		if self.location:
			return {'x': self.location['x'], 'y' : self.location['y']-1}

	def right(self):
		if self.location:
			return {'x': self.location['x'], 'y' : self.location['y']+1}			

	def up(self): 
		if self.location:
			return {'x': self.location['x']-1, 'y' : self.location['y']}

	def down(self):
		if self.location:
			return {'x': self.location['x']+1, 'y' : self.location['y']}

	

class Graph:
	def __init__(self,file):
		self.file = file
		self.grid = []
		self.edges = []
		self.connections = []
		self.connection_count = 0
		self.grid_length = 0
		self.make_grid()
	
	def make_grid(self):	
		line = []
		x,y = 0,0
		
		with open(filename) as f:
			
			while True:
				
				c = f.read(1)

				if c == '\n':
					self.grid.append(line)
					line = []
					x += 1
					y = 0
					self.grid_length += 1
				elif c == "#":
					v = Vertex()
					v.id = "#"
					v.location = {'x' : x, 'y' : y}
					line.append(v)
					y += 1
				elif c == "_":
					self.connection_count += 1
					v = Vertex()
					v.id = "_"
					v.location = {'x' : x, 'y' : y}
					v.open = True
					self.edges.insert(0,v)
					line.append(v)
					
					y += 1
				
				if not c:
					break

		self.__find_connections()

	def search_connections(self,node):
		for key_node in self.connections:
			if key_node.keys()[0] == node:
				return key_node

	def theres_an_end_of_maze(self):
		return [x for x in self.grid[0] if x.id == "_"]


	def show_grid(self):
		x,y = 0,0
		
		for x in range(self.grid_length-1):
			for y in range(self.__col_length()):
				print self.grid[x][y].location

	def get_node(self,location):
		if (location['y'] > self.__col_length() 
			or location['y'] < 0 
			or location['x'] > self.grid_length-1 
			or location['x'] < 0):
				return Vertex()
		else:	
			return self.grid[location['x']][location['y']]

	# private
	
	def __col_length(self):
		return len(self.grid[0])-1

	def __find_connections(self):
		if self.grid:

			for path in self.edges:
				con = {}	
				con[path] = {
					'node' : path,
					'connections' : []
				}

				up    = self.get_node(path.up())
				down  = self.get_node(path.down())
				left  = self.get_node(path.left())
				right = self.get_node(path.right())

				
				if up.open: con[path]['connections'].append(up)
				if down.open: con[path]['connections'].append(down)
				if left.open: con[path]['connections'].append(left)
				if right.open: con[path]['connections'].append(right)
				
				self.connections.append(con)
		else:
			print 'grid hasnt been initialized yet.'

	
class Traverse:
	def __init__(self,file):
		self.graph = Graph(file)
		self.path = []
		
	def bfs(self):
		if self.graph.theres_an_end_of_maze():
			start = self.graph.connections[0]
			queue = [start]
			self.path.append(start)
			
			end = self.graph.grid[0][3].location
			next_to_last = self.graph.grid[1][3].location
			
			while queue:
				current_node = queue.pop(0)

				for adj in current_node.values()[0]['connections']:
					
					next_node = self.graph.search_connections(adj)
					
					if (next_node.keys()[0].location    == end 
						or next_node.keys()[0].location == next_to_last):
						self.path.append(next_node)
						if self.path[-1] == next_node:
							final_node = self.graph.search_connections(self.graph.grid[0][3])
							self.path.append(final_node)
						return self
					elif next_node not in self.path:
						queue.insert(0,next_node)
						self.path.append(next_node)	
		else:
			print 'there is not a way out of the maze'

				
	

		

		
			



		





				





filename = '../test_mazes.txt'

path = Traverse(filename)

for x in path.bfs().path:
	print x.keys()[0].location



















