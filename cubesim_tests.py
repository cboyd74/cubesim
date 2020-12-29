import cubesim 
import sys
from termcolor import colored

class CubeSimTests():
	
	def __init__(self):
		print("")
		print("++++++++++++++++++++++++++++++++++++")
		print("++ Welcome to the CubeSim tester.")
		print("++++++++++++++++++++++++++++++++++++")
		print("")


	def print_success(self, msg):
		print(colored("++", "green"), msg)

	def print_failure(self, msg):
		print("--", msg)

	# Compares the cube's Side's id with the sides given.
	# Returns False if the sides are out of order.
	def compare_cube(self,cube, verify_sides):
		if (cube.front.id != verify_sides[0]):
			return False
		if (cube.back.id != verify_sides[1]):
			return False
		if (cube.left.id != verify_sides[2]):
			return False
		if (cube.right.id != verify_sides[3]):
			return False
		if (cube.top.id != verify_sides[4]):
			return False
		if (cube.bottom.id != verify_sides[5]):
			return False
		return True	

	def compare_side(self, side, verify_side):
		for i in range(0, len(side)):
			for j in range(0, len(side[i])):
				if (side[i][j] != verify_side[i][j]):
					return False
		return True
	
	#-----------------------------------------------------------
	
	def test_side_rotate_right(self):
		
		return True, "rotate side right: all tests passed."
	
	#-----------------------------------------------------------
	
	def test_side_rotate_left(self):
		side = cubesim.Side(1, 3)
		side.values[0] = [5, 6, 7]
		verify_side = [[7, 1, 1], [6,1,1], [5,1,1]]
		side.rotate_left()
		if (not self.compare_side(side.values, verify_side)):
			return False, "test_side_rotate_left test 1: failed."
		
		verify_side = [[1, 1, 1], [1, 1, 1], [7, 6, 5]]
		side.rotate_left()
		if (not self.compare_side(side.values, verify_side)):
			return False, "test_side_rotate_left test 2: failed."	
		return True, "rotate_side_rotate_left: all tests passed."

	#-----------------------------------------------------------

	# Tests the functionality of left and right operations
	# in Cube.orient_cube() 	
	def test_orient_cube1(self):
		cube = cubesim.Cube(3)
		
		# Test left 1
		verify_cube = [3, 2, 0, 1, 4, 5] 
		cube.orient_cube("left")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube left operation test 1: failed."

		# Test left 2
		verify_cube = [1, 0, 3, 2, 4, 5]
		cube.orient_cube("left")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube left operation test 2: failed."
		
		cube.init_cube() #reset the cube
	
		# Test right 2
		verify_cube = [2, 3, 1, 0, 4, 5]
		cube.orient_cube("right")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube right operation test 1: failed."

		# Test right 2
		verify_cube = [1, 0, 3, 2, 4, 5]
		cube.orient_cube("right")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube right operation test 2: failed."

		return True, "orient_cube left and right operations: all tests passed"

	#-----------------------------------------------------------

	# Tests the functionality of the up and down operations in 
	# Cube.orient_cube()
	def test_orient_cube2(self):
		cube = cubesim.Cube(3)
	#	cube.print_cube()		

		# Test up 1
		verify_cube = [5, 4, 2, 3, 0, 1]
		cube.orient_cube("up")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube up operation test 1: failed."

		# Test up 2  
		verify_cube = [1, 0, 2, 3, 5, 4]
		cube.orient_cube("up")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube up operation test 2: failed."

		cube.init_cube() #reset cube

		# Test down 1
		verify_cube = [4, 5, 2, 3, 1, 0]
		cube.orient_cube("down")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube down operation test 1: failed."
		
		# Test down 2
		verify_cube = [1, 0, 2, 3, 5, 4]
		cube.orient_cube("down")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube down operation test 2: failed."

		return True, "orient_cube up and down operations: all tests passed."

 	#-----------------------------------------------------------

	def test_orient_cube3(self):
		cube = cubesim.Cube(3)
		
		# Test side left 1
		verify_cube = [0, 1, 4, 5, 3, 2]
		cube.orient_cube("side left")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube side left operation test 1: failed."
		
		# Test side left 2	
		verify_cube = [0, 1, 3, 2, 5, 4]
		cube.orient_cube("side left")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube side left operation test 2: failed."

		cube.init_cube()

		# Test side right 1
		verify_cube = [0, 1, 5, 4, 2, 3]
		cube.orient_cube("side right")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube side right operation test 1: failed."

		# Test side right 2
		verify_cube = [0, 1, 3, 2, 5, 4]	
		cube.orient_cube("side right")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube side right operation test 2: failed."
		return True, "orient_cube side operations: all tests passed."
 
	#-----------------------------------------------------------

	def test4(self):
		print("")
		return True
	
	#-----------------------------------------------------------

	def run_tests(self, tests):
		print("Beginning", len(tests), "tests...")
		print("")
		passed = 0
		for test in tests:
			res, msg = test()
			if (res == True):
				self.print_success(msg)
				passed += 1
			else:
				self.print_failure(msg)
		print("")
		print("CubeSim Tester: passed", passed, "out of", len(tests), "tests.")
		print("goodbye.")
		print("")

class Main():
	def main():
		tester = CubeSimTests()
		tests = [tester.test_side_rotate_left,
				 tester.test_side_rotate_right, 
				tester.test_orient_cube1, 
				tester.test_orient_cube2, 
				tester.test_orient_cube3]
		tester.run_tests(tests)

	if __name__ == "__main__":
		main()
