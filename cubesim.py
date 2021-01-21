import numpy as np
import sys
from termcolor import colored

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
 
	def __init__(self, n):
		max_size = 8
		min_size = 2
		default_size = 3
		self.colors = ["white", "yellow", "red", "magenta", "green", "blue"]
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
	
	# Reorients the cube in the given direction: up, down, left, right
	def orient(self, direction):

		if (direction == "up"):
			tmp = self.front
			self.front = self.bottom #bottom becomes front
			tmp2 = self.top
			tmp2.rotate_right()
			tmp2.rotate_right()
			self.top = tmp #front becomes top
			tmp = self.back
			tmp.rotate_right()
			tmp.rotate_right()
			self.back = tmp2 #top becomes back
			self.bottom = tmp # back becomes bottom
			self.left.rotate_left() # rotate left side
			self.right.rotate_right() # rotate right side

		elif (direction == "down"):
			tmp = self.back
			tmp.rotate_right()
			tmp.rotate_right()
			self.back = self.bottom # bottom becomes back
			self.back.rotate_right()
			self.back.rotate_right()
			tmp2 = self.top
			self.top = tmp # back becomes top
			tmp = self.front
			self.front = tmp2 # top becomes front
			self.bottom = tmp # front becomes bottom
			self.left.rotate_right() # rotate left side
			self.right.rotate_left() # rotate right side

		elif(direction == "left"): # move cube left
			tmp = self.front
			self.front = self.right # right becomes front
			tmp2 = self.left
			self.left = tmp # front becomes left
			tmp = self.back
			self.back = tmp2 # left becomes back
			self.right = tmp # back becomes right
			self.top.rotate_right()# rotate top 
			self.bottom.rotate_left() # rotate bottom

		elif(direction == "right"): #move cube right
			tmp = self.front	
			self.front = self.left # left becomes front
			tmp2 = self.right
			self.right = tmp # front becomes right 
			tmp = self.back
			self.back = tmp2 # right becomes back
			self.left = tmp # back becomes left
			self.top.rotate_left() # rotate top 
			self.bottom.rotate_right() # rotate bottom

		elif (direction == "side left"):
			tmp = self.top
			tmp.rotate_left() 
			self.top = self.right # top becomes right
			self.top.rotate_left()
			tmp2 = self.left
			tmp2.rotate_left() 
			self.left = tmp # left becomes top
			tmp = self.bottom 
			tmp.rotate_left()
			self.bottom = tmp2 # bottom becomes left
			self.right = tmp # right becomes bottom
			self.front.rotate_left() # rotate front
			self.back.rotate_right() # rotate back	

		elif (direction == "side right"):
			tmp = self.top
			tmp.rotate_right()
			self.top = self.left
			self.top.rotate_right()
			tmp2 = self.right
			tmp2.rotate_right()
			self.right = tmp
			tmp = self.bottom
			tmp.rotate_right() #rotate right to adjust layout
			self.bottom = tmp2
			self.left = tmp
			self.front.rotate_right() # rotate front
			self.back.rotate_left() # rotate back

		else: # input error
			print("orient_cube: input error!")
	
	def move(self, face, top, bottom, left, right):
		#rotate front right
		face.rotate_right()

        #top's last row becomes first column of right (in order)
		tmp = []
		for i in range(0, self.size):
			tmp.append(right.values[i][0]) #save right's first column
			right.values[i][0] = top.values[self.size-1][i] #set right's first column

        #first column of right becomes first row of bottom (in reverse)
		tmp2 = []
		j = self.size-1 
		for i in range(0, self.size):
			tmp2.append(bottom.values[0][i]) #save bottom's first  
			bottom.values[0][i] = tmp[j] #set bottom's first column (reverse)
			j-=1

        #first row of bottom becomes last column of left (in order)
		tmp = []
		for i in range(0, self.size):
			tmp.append(left.values[i][self.size-1]) #save left's last column 
			left.values[i][self.size-1] = tmp2[i] #set left's first column (reverse)

        #last column of left becomes last row of top (in reverse)
		j = self.size-1
		for i in range(0, self.size):
			top.values[self.size-1][i] = tmp[j]
			j-=1

	def prime(self, face, top, bottom, left, right):
		#rotate front left
		face.rotate_left()

        #top's last row becomes last column of left (in reverse)

        #left's last column becomes bottom's first row (in order)

        #bottom's first row becomes right's first column (in reverse)

        #right's first column becomes top's bottom row (in order)

	#peforms the specified move, changes state of cube	
	def make_move(self, side, p):
		print("")
		
		#front
		if (side == "f"):
			if (p == 1):
				self.prime(self.front, self.top, self.bottom, self.left, self.right)
			else:
				self.move(self.front, self.top, self.bottom, self.left, self.right) 
		#right
		elif (side == "r"):
			if (p == 1):
				self.prime(self.right, self.top, self.bottom, self.front, self.back)
			else:
				self.move(self.right, self.top, self.bottom, self.front, self.back)
		#left 
		elif (side == "l"):
			if(p == 1):
				self.prime(self.left, self.top, self.bottom, self.back, self.front)
			else:
				self.move(self.left, self.top, self.bottom, self.back, self.front)
		#up
		elif (side == "u"):
			if (p == 1):
				self.prime(self.top, self.back, self.front, self.left, self.right)
			else:
				self.move(self.top, self.back, self.front, self.left, self.right)
		#down
		elif (side == "d"):
			if (p == 1):
				self.prime(self.bottom, self.front, self.back, self.left, self.right)
			else:
				self.move(self.bottom, self.front, self.back, self.left, self.right) 
		#back
		elif (side == "b"):
			if (p == 1):
				self.prime(self.back, self.top, self.bottom, self.right, self.left)
			else:
				self.move(self.back, self.top, self.bottom, self.right, self.left)

	#Output stuff
	def print_row(self, side, i):
		for j in range(0, self.size):
			value = side.values[i][j]
			print(colored(value, self.colors[value]), sep = "", end = " ")
	
	def print_cube(self):
		print("- - - - - - - - - - - - - - - - - - - - - -")
		print(" - - - - - - - - - - - - - - - - - - - - -")

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

		print(" - - - - - - - - - - - - - - - - - - - - -")
		print("- - - - - - - - - - - - - - - - - - - - - -")

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
	def rotate_right(self):
		new_values = np.full((self.size, self.size), self.values)
		row = 0
		col = self.size-1 
		for i in range(0, self.size):
			for j in range(0, self.size):
				 new_values[row][col] = self.values[i][j]
				 row += 1
			row = 0
			col -= 1
		self.values = new_values

	def rotate_left(self):
		new_values = np.full((self.size, self.size), self.values)
		row = 0
		col = 0 
		for i in range(0, self.size):
			for j in range(self.size-1, -1, -1):
				new_values[row][col] = self.values[i][j]
				row += 1
			row = 0
			col += 1
		self.values = new_values	

class Sim:
	def __init__(self):
		print("Welcome to CubeSim")
		self.cube = Cube(3)
		self.main()

	def main(self):
		cube = Cube(3)
		self.cubing(self.cube)

	def cubing(self, cube):
		cube.print_cube()

		while (1):
			print(":::", end = " ")
			inp = input()
			if (inp == "Q" or inp == "q"):
				break

			if (len(inp) > 3): #error if command has more than 2 characters
				print("Error: command not recognized")
			else:	
				if (inp == "ou"): #orient up
					cube.orient("up")
				elif (inp == "od"): #orient down
					cube.orient("down")	
				elif (inp == "or"): #orient right
					cube.orient("right")	
				elif (inp == "ol"): #orient down
					cube.orient("left")	
				elif (inp == "osr"): #orient side right
					cube.orient("side right")
				elif (inp == "osl"): #orient side left
					cube.orient("side left")
				elif (inp == "mf"):
					cube.make_move("f", 0)
				elif (inp == "mr"):
					cube.make_move("r", 0)
				elif (inp == "ml"):
					cube.make_move("l", 0)
				elif (inp == "mu"):
					cube.make_move("u", 0)
				elif (inp == "md"):
					cube.make_move("d", 0)
				elif(inp == "mb"):
					cube.make_move("b", 0)
				else:
					print("Error: command not recognized")

			cube.print_cube()
