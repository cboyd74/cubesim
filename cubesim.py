import numpy as np
import sys

class Cube:
	# internal represenation of the cube:
	#
	#          444
	#          444 
	#          444
	#      222 000 333    111
	#      222 000 333    111
	#      222 000 333    111
	#          555
    #          555
    #          555
	#
	# As shown above, for each even numbered index i, the odd index
	# i + 1 is i's opposite side
	#
	# Data structure: the cube will be a numpy array in which each element
	#                 is a numpy matrix representing a side of the cube
	#
	#	cube =  [ [0,0,0]  [1,1,1]          [5,5,5]
	#			  [0,0,0]  [1,1,1]          [5,5,5]
	#			  [0,0,0], [1,1,1], . . . . [5,5,5] ]
 
	def __init__(self, size):
		max_size = 4
		min_size = 2
		default_size = 3
		
		if (size <= max_size and size >= min_size):
			self.size = size
		else: 
			self.size = default_size
		self.cube = [] 
		side = 0
		for i in range(0, 6):
			self.cube.append(np.full((self.size, self.size), side))
			side += 1
		self.cube = np.array(self.cube) 
	
	#peforms the specified move, changes state of cube	
	def move(component, direction):
		#front to the right
		print("")

	def get_opposite_side(self, side):
		if (side % 2 == 0): #is an even side
			return self.cube[side+1]
		return self.cube[size-1] 
	
	def print_cube(self):
		print("================================")
		print("current state of the cube")
		print("================================")
		for i in range(0, self.size):
			for h in range(0, self.size+7):
				print(" ", sep = "", end = "")
			for j in range(0, self.size):
				if (j == self.size - 1):
					print(self.cube[4][i][j], sep = "")
				else:
					print(self.cube[4][i][j], sep = "", end = " ")
		#print sides 2, then 0, then 3, then 1
		for i in range(0, self.size):
			print("   ", sep = "", end = "")
			for j in range(0, self.size):
				if (j == self.size - 1):
					print(self.cube[2][i][j], sep = "", end = "")
					continue
				print(self.cube[2][i][j], sep = "", end = " ")
			print("  ", end = "")
			for j in range(0, self.size):
				if (j == self.size - 1):
					print(self.cube[0][i][j], sep = "", end = "")
					continue
				print(self.cube[0][i][j], sep = "", end = " ")
			print("  ", end = "")
			for j in range(0, self.size):
				if (j == self.size - 1):
					print(self.cube[3][i][j], sep = "", end = "")
					continue
				print(self.cube[3][i][j], sep = "", end = " ")
			print("    ", end = "")
			for j in range(0, self.size):
				if (j == self.size - 1):
					print(self.cube[1][i][j], sep = "", end = "")
					continue
				print(self.cube[1][i][j], sep = "", end = " ")
			print("")
		#print side 5 on bottom		
		for i in range(0, self.size):
 			for h in range(0, self.size+7):
 				print(" ", sep = "", end = "")
 			for j in range(0, self.size):
 				if (j == self.size - 1):
 					print(self.cube[5][i][j], sep = "")
 				else:
 					print(self.cube[5][i][j], sep = "", end = " ")
		print("================================")
		print("================================")
class Sim:
	def main():
		cube = Cube(3)
		cube.print_cube()
	if __name__ == "__main__":
		main()
