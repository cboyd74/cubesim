import numpy as np
import sys

# This class serves as a model for a Rubik's Cube, made up of Sides
class Cube:

	# members
	#  |-- size:    size n for an n x n cube
	#  |-- sides:   list of sides, currently [front, back, left, right, top, bottom]
	#  |-- front:   side currently being looked at
	#  |-- back:    side currently to the back of the cube
	#  |-- left:    side currently on the left side of the cube
	#  |-- right:   side currently on the right side of the cube
    #  |-- top:     side currently on the top of the cube
	#  |-- bottom:  side currently on the bottom of the cube
 
	#---------------------------------------------------------------

	def __init__(self, n):
		max_size = 8
		min_size = 2
		default_size = 3
		if (n <= max_size and n >= min_size):
			self.size = n 
		else: 
			self.size = default_size
		self.sides = None 
		self.init_cube()

	def init_cube(self):
		self.front = Side(0, self.size)
		self.back = Side(1, self.size)
		self.left = Side(2, self.size)
		self.right = Side(3, self.size)
		self.top = Side(4, self.size)
		self.bottom = Side(5, self.size)
	
	#---------------------------------------------------------------

	# Reorients the cube in the given direction: up, down, left, right
	def orient_cube(self, direction):
		# move cube up
		if (direction == "up"):
			tmp = self.front
			self.front = self.bottom #bottom becomes front
			tmp2 = self.top
			self.top = tmp #front becomes top
			tmp = self.back
			self.back = tmp2 #top becomes back
			self.bottom = tmp # back becomes bottom
		# move cube down	
		elif (direction == "down"):
			tmp = self.back
			self.back = self.bottom # bottom becomes back
			tmp2 = self.top
			self.top = tmp # back becomes top
			tmp = self.front
			self.front = tmp2 # top becomes front
			self.bottom = tmp # front becomes bottom
		# move cube left	
		elif(direction == "left"): # move cube left
			tmp = self.front
			self.front = self.right # right becomes front
			tmp2 = self.left
			self.left = tmp # front becomes left
			tmp = self.back
			self.back = tmp2 # left becomes back
			self.right = tmp # back becomes right
		# move cube right
		elif(direction == "right"): #move cube right
			tmp = self.front	
			self.front = self.left # left becomes front
			tmp2 = self.right
			self.right = tmp # front becomes right 
			tmp = self.back
			self.back = tmp2 # right becomes back
			self.left = tmp # back becomes left
		elif (direction == "side left"):
			tmp = self.top
			self.top = self.right
			tmp2 = self.left
			self.left = tmp
			tmp = self.bottom
			self.bottom = tmp2
			self.right = tmp
		
		elif (direction == "side right"):
			tmp = self.top
			self.top = self.left
			tmp2 = self.right
			self.right = tmp
			tmp = self.bottom
			self.bottom = tmp2
			self.left = tmp
		else: #Error
			print("orient_cube: input error!")

	#peforms the specified move, changes state of cube	
	def move(component, direction):
		#front to the right
		print("")

	#---------------------------------------------------------------

	#Output stuff
	def print_row(self, side, i):
		for j in range(0, self.size):
			print(side.values[i][j], sep = "", end = " ")
	
	def print_cube(self):
		print("+++++++++++++++++++++++++++++++++++++++")
		#print top
		for i in range(0, self.size):
			for h in range(0, self.size+8): #for spacing
				print(" ", sep = "", end = "")
			self.print_row(self.top, i)
			print("")
		#print sides 2, then 0, then 3, then 1
		for i in range(0, self.size):
			print("   ", sep = "", end = "")
			self.print_row(self.left, i) #print 2
			print("  ", end = "")
			self.print_row(self.front, i)
			print("  ", end = "")
			self.print_row(self.right, i)
			print("    ", end = "")
			self.print_row(self.back, i)
			print("")
		#print side 5 on bottom		
		for i in range(0, self.size):
			for h in range(0, self.size+8):
				print(" ", sep = "", end = "")
			self.print_row(self.bottom, i)
			print("")
		print("+++++++++++++++++++++++++++++++++++++++")

	#---------------------------------------------------------------

class Side:

	# members
	#  |--	values:    2D numpy matrix	
	#  |--	id:        ID of this side (0 - 5)
	#  |--  neighbors: 
	#
	def __init__(self, id, size):
		self.size = size
		self.id = id
		self.values = np.full((self.size, self.size), self.id)

	# Function to rotate the values of the cube
	#  either left 90 or right 90
	#  1 2   -->  3 1       1 2  -->  2 4
	#  3 4        4 2   or  3 4       1 3

class Sim:
	def __init__(self):
		print("Welcome to CubeSim")
		self.main()

	def main(self):
		cube = Cube(3)
		self.cubing(cube)

	def cubing(self, cube):
		inp = input()
		while (inp != "q" and inp != "Q"):
			if (len(inp) > 2): #error if command has more than 2 characters
				print("Error: command not recognized")

 
