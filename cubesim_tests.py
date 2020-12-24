import cubesim 

class CubeSimTests():
	
	def __init__(self):
		print("TESTING CUBESIM.PY")

	#-----------------------------------------------------------

	def print_success(self, test_name):
		print("************************************")
		print("** SUCCESS.")
		print("************************************")                 

	#-----------------------------------------------------------
	
	def print_failure(self, test_name):
		print("************************************")
		print("** FAILURE.")
		print("************************************")

	#-----------------------------------------------------------	
	
	# Compares the cube's Side's id with the sides given.
	# Returns False if the sides are out of order.
	def compare_cube(self,cube, verify_sides):
		test_sides = cube.sides
		for i in range(0, 6):
			if (test_sides[i].id != verify_sides[i]):
				return False
		return True	

	#-----------------------------------------------------------
	#-----------------------------------------------------------

	# Tests the functionality of left and right operations
	# in Cube.orient_cube() 	
	def test_orient_cube1(self):
		cube = cubesim.Cube(3)
	#	cube.print_cube()
		
		# Test left 1
		verify_cube = [2, 3, 1, 0, 4, 5] 
		cube.orient_cube("left")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube() left operation test 1: failed."

		# Test left 2
		verify_cube = [1, 0, 3, 2, 4, 5]
		cube.orient_cube("left")
		if (not self.compare_cube(cube, verify_cube)):
			return False, "orient_cube left operation test 2: failed."
		
		cube.init_cube() #reset the cube
	
		# Test right 2
		verify_cube = [3, 2, 0, 1, 4, 5]
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

	def test3(self):
		print("")
		return True
	#-----------------------------------------------------------

	def test4(self):
		print("")
		return True
	
	#-----------------------------------------------------------

	def run_tests(self, tests):
		for test in tests:
			res, msg = test()
			if (res == True):
				self.print_success(str(test))
				print(msg)
				print("************************************")
			else:
				self.print_failure(str(test))
				print(msg)
				print("************************************")

class Main():
	def main():
		tester = CubeSimTests()
		tests = [tester.test_orient_cube1]
		tester.run_tests(tests)

	if __name__ == "__main__":
		main()
