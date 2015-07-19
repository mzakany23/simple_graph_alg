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

		self.__generate_connections()

	def search_connections(self,node):
		for key_node in self.connections:
			if key_node.keys()[0] == node:
				return key_node

	def maze_end(self):
		return [x for x in self.grid[0] if x.id == "_"]


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

	def __generate_connections(self):
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
		self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		self.path = []
		
	def traverse_file(self):
		''' sort of like breadth first search'''

		if self.graph.maze_end():
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
						return 
					elif next_node not in self.path:
						queue.insert(0,next_node)
						self.path.append(next_node)	
		else:
			print 'there is not a way out of the maze'


	def show_route(self):
		''' start from bottom and go up'''

		output = ""
		self.traverse_file()
		connections = self.path
		g = self.graph

		x,y,i = 0,0,0
		x = len(g.grid)-1

		# circular array
		if i == 26: i = 0

		# location dict to check against
		d = {}
		
		for found in self.path:
			loc = str(found.keys()[0].location)
			d[loc] = found

		location_dict_keys = d.keys()

		while x > -1:
			line = ""

			for y in range(len(g.grid[0])-1):

				# last column
				if y == 5:
					if g.grid[x][y].id == '_':
						if str(g.grid[x][y].location) in location_dict_keys:
							line += self.alphabet[i]
							i += 1
						else:
							line += '_'
					else:
						line += '#'

					line += '#'
					line += '\n'
					new_output = line + output
					output = new_output
					
				elif g.grid[x][y].id == '_':
					if str(g.grid[x][y].location) in location_dict_keys:
						line += self.alphabet[i]
						i += 1
					else:
						line += '_'
				else:
					line += '#'

			x -= 1

		return output






		





				





filename = '../test_mazes.txt'

path = Traverse(filename)

# print path.show_route()
















