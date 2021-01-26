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
		
		self.front.init_borders(self.top.values[self.size-1, :].copy(), self.left.values[:, self.size-1].copy(), self.right.values[:, 0].copy(), self.bottom.values[0, :].copy())

		self.back.init_borders(np.flip(self.top.values[self.size-1, :].copy()), self.right.values[:, self.size-1].copy(), self.left.values[:, 0].copy(), np.flip(self.bottom.values[self.size-1, :].copy()))

		self.left.init_borders(self.top.values[0, :].copy(), self.back.values[:, self.size-1], self.front.values[:, 0], np.flip(self.bottom.values[:, 0].copy()))

		self.right.init_borders(np.flip(self.top.values[:, self.size-1].copy()), self.front.values[:, self.size-1].copy(), self.back.values[:, 0].copy(), self.bottom.values[:, self.size-1].copy())

		self.top.init_borders(np.flip(self.back.values[0, :].copy()), self.left.values[0,:], np.flip(self.right.values[0, :].copy()), self.front.values[0,:])

		self.bottom.init_borders(self.front.values[self.size-1,:].copy(), np.flip(self.left.values[self.size-1,:].copy()), self.right.values[self.size-1, :].copy(), np.flip(self.back.values[self.size-1,:].copy()))

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
			self.back = self.bottom
			self.back.rotate_right()
			self.back.rotate_right()
			tmp2 = self.top
			self.top = tmp
			tmp = self.front
			self.front = tmp2
			self.bottom = tmp
			self.left.rotate_right()
			self.right.rotate_left()

		elif(direction == "left"): 
			tmp = self.front
			self.front = self.right 
			tmp2 = self.left
			self.left = tmp
			tmp = self.back
			self.back = tmp2 
			self.right = tmp 
			self.top.rotate_right() 
			self.bottom.rotate_left()

		elif(direction == "right"):
			tmp = self.front	
			self.front = self.left
			tmp2 = self.right
			self.right = tmp  
			tmp = self.back
			self.back = tmp2 
			self.left = tmp 
			self.top.rotate_left() 
			self.bottom.rotate_right()

		elif (direction == "side left"):
			tmp = self.top
			tmp.rotate_left() 
			self.top = self.right 
			self.top.rotate_left()
			tmp2 = self.left
			tmp2.rotate_left() 
			self.left = tmp 
			tmp = self.bottom 
			tmp.rotate_left()
			self.bottom = tmp2 
			self.right = tmp 
			self.front.rotate_left() 
			self.back.rotate_right()

		elif (direction == "side right"):
			tmp = self.top
			tmp.rotate_right()
			self.top = self.left
			self.top.rotate_right()
			tmp2 = self.right
			tmp2.rotate_right()
			self.right = tmp
			tmp = self.bottom
			tmp.rotate_right() 
			self.bottom = tmp2
			self.left = tmp
			self.front.rotate_right()
			self.back.rotate_left()

		else: # input error
			print("orient_cube: input error!")
	
	def move(self, face, top, bottom, left, right):
		#rotate front right
		face.rotate_right()

        #top's last row becomes first column of right (in order)
		tmp = face.right_border.copy()
		face.right_border = face.top_border
        #first column of right becomes first row of bottom (in reverse)
		tmp2 = face.bottom_border.copy() 
		face.bottom_border = np.flip(tmp)
        #first row of bottom becomes last column of left (in order)
		tmp = face.left_border.copy()
		face.left_border = tmp2 
        #last column of left becomes last row of top (in reverse)
		face.top_border = np.flip(tmp)
		#Update side values
		for i in range(0, self.size):
			top.values[self.size-1][i] = face.top_border[i]
			left.values[i][self.size-1] = face.left_border[i]
			right.values[i][0] = face.right_border[i]
			bottom.values[0][i] = face.bottom_border[i]

	def prime(self, face, top, bottom, left, right):
		#rotate front left
		face.rotate_left()
        #top's last row becomes last column of left (in reverse)
        #left's last column becomes bottom's first row (in order)
        #bottom's first row becomes right's first column (in reverse)
        #right's first column becomes top's bottom row (in order)

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
	#  |--	values:          2D numpy matrix	
	#  |--	id:              ID of this side (0 - 5)
	#  |--  top_border:      numpy array of values bordering top
	#  |--  left_border:     
	#  |--  right_border:
	#  |--  bottom_border:  

	def __init__(self, id, size):
		self.size = size
		self.id = id
		self.values = np.full((self.size, self.size), self.id)
		self.top_border = np.zeros(self.size) 
		self.left_border = np.zeros(self.size) 
		self.right_border = np.zeros(self.size) 
		self.bottom_border = np.zeros(self.size) 

	def init_borders(self, top, left, right, bottom):
		self.top_border = top
		self.left_border = left
		self.right_border = right
		self.bottom_border = bottom
	
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
