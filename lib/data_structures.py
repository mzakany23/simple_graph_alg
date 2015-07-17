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
					v.location = {'x' : x, 'y' : y}
					line.append(v)
					y += 1
				elif c == "_":
					self.connection_count += 1
					v = Vertex()
					v.location = {'x' : x, 'y' : y}
					v.open = True
					self.edges.insert(0,v)
					line.append(v)
					
					y += 1
				
				if not c:
					break

		self.__find_connections()

	# private
	def __get_node(self,location):
		if (location['y'] > self.__col_length 
			or location['y'] < 0 
			or location['x'] > self.grid_length-1 
			or location['x'] < 0):
				return Vertex()
		else:	
			return self.grid[location['x']][location['y']]

	def __col_length(self):
		return len(self.grid[0])-self.grid_length-1

	def __find_connections(self):
		if self.grid:
		
			for path in self.edges:
				con = {
					'node' : path,
					'connections' : []
				}

				up    = self.__get_node(path.up())
				down  = self.__get_node(path.down())
				left  = self.__get_node(path.left())
				right = self.__get_node(path.right())
				
				if up.open: con['connections'].append(up)
				if down.open: con['connections'].append(down)
				if left.open: con['connections'].append(left)
				if right.open: con['connections'].append(right)
				
				
				self.connections.append(con)
		else:
			print 'grid hasnt been initialized yet.'

	
 

filename = '../test_mazes.txt'

g = Graph(filename)

g.make_grid()
















