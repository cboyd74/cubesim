import numpy as np
import sys

# This class serves as a model for a Rubik's Cube, made up of Sides
class Cube:
 
	#---------------------------------------------------------------

	def __init__(self, size):
		max_size = 8
		min_size = 2
		default_size = 3
		
		if (size <= max_size and size >= min_size):
			self.size = size
		else: 
			self.size = default_size
		self.sides = []
		self.init_cube()
		self.looking_at = self.sides[0] 

	def init_cube(self):
		side = 0
		for i in range(0, 6):
			self.sides.append(Side(i, self.size))
			side += 1
		self.sides = np.array(self.sides)
	
	#---------------------------------------------------------------

	# Reorients the cube in the given direction: up, down, left, right
	def orient_cube(self, direction):	
		print("")	

	#peforms the specified move, changes state of cube	
	def move(component, direction):
		#front to the right
		print("")

	#---------------------------------------------------------------

	#Output stuff
	def print_row(self, side, i):
		for j in range(0, self.size):
			current = self.sides[side].values
			print(current[i][j], sep = "", end = " ")
	
	def print_cube(self):

		print("================================")
		print("current state of the cube")
		print("================================")
		
		#print side 4 on top
		for i in range(0, self.size):
			for h in range(0, self.size+8): #for spacing
				print(" ", sep = "", end = "")
			self.print_row(4, i)
			print("")
		#print sides 2, then 0, then 3, then 1
		for i in range(0, self.size):
			print("   ", sep = "", end = "")
			self.print_row(2, i) #print 2
			print("  ", end = "")
			self.print_row(0, i)
			print("  ", end = "")
			self.print_row(3, i)
			print("    ", end = "")
			self.print_row(1, i)
			print("")
		#print side 5 on bottom		
		for i in range(0, self.size):
			for h in range(0, self.size+8):
				print(" ", sep = "", end = "")
			self.print_row(5, i)
			print("")
		print("================================")
		print("================================")

	#---------------------------------------------------------------

class Side:

	# members
	#	values --> 2D numpy matrix	
	#	id     --> ID of this side (0 - 5)
	#
	def __init__(self, id, size):
		self.size = size
		self.id = id
		self.values = np.full((self.size, self.size), self.id) 

class Sim:
	def main():
		cube = Cube(3)
		cube.print_cube()
	#if __name__ == "__main__":
	#	main()
