import sys
sys.path.append('lib/')

from data_structures import Traverse


maze_1 = 'mazes/test_maze_1.txt'
maze_2 = 'mazes/test_maze_2.txt'
maze_3 = 'mazes/test_maze_3.txt'
maze_4 = 'mazes/test_maze_4.txt'

mazes = [maze_1,maze_2,maze_3,maze_4]

def run_mazes(*arg):
	for maze in mazes:
		print "---------------------------------------------------------------------------"
		print "Maze %s" % maze
		print ' '
		print Traverse(maze).show_route()

run_mazes(mazes)
