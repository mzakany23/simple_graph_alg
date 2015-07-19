import sys
sys.path.append('lib/')

from data_structures import Traverse


file = 'test_maze.txt'
t = Traverse(file)

print t.show_route()