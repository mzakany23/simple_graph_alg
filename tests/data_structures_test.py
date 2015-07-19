import unittest
import sys
sys.path.append('../lib')
from data_structures import Vertex,Graph,Traverse


class TestVertex(unittest.TestCase):

	def setUp(self):
			v = Vertex()
			v.location = {'x' : 4, 'y' : 1}
			self.v = v
			
	def test_returns_the_position_to_the_left(self):
		assert self.v.left() == {'x' : 4, 'y' : 0}



class TestGraph(unittest.TestCase):
	def setUp(self):
		file = '../mazes/test_maze_1.txt'
		self.g = Graph(file)

	def test_make_sure_init_fills_instance_variables(self):
		assert len(self.g.grid) > 0



class TestTraverse(unittest.TestCase):
	def setUp(self):
		file = '../mazes/test_maze_1.txt'
		self.t = Traverse(file)

	def test_traverse_file_and_fill_path_instance_variable(self):
		'''  this creates a connection list'''
		assert len(self.t.traverse_file().path) > 0

	def test_get_location_dict(self):
		''' have to run traverse file first to fill the path list'''
		self.t.traverse_file()
		assert len(self.t.get_location_dict()) > 0


	

if __name__ == '__main__':
    unittest.main()

