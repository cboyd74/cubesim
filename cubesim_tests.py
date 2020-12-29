import cubesim 

class CubeSimTests():
	
	def __init__(self):
		print("++++++++++++++++++++++++++++++++++++")
		print("++ Welcome to the CubeSim tester.")
		print("++++++++++++++++++++++++++++++++++++")

	#-----------------------------------------------------------

	def print_success(self, msg):
		print("++", msg)

	#-----------------------------------------------------------
	
	def print_failure(self, msg):
		print("--", msg)

	#-----------------------------------------------------------	
	
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

	#-----------------------------------------------------------

	# Tests the functionality of left and right operations
	# in Cube.orient_cube() 	
	def test_orient_cube1(self):
		cube = cubesim.Cube(3)
	#	cube.print_cube()
		
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
		passed = 0
		for test in tests:
			res, msg = test()
			if (res == True):
				self.print_success(msg)
				passed += 1
			else:
				self.print_failure(msg)
		print("CubeSim Tester: passed", passed, "out of", len(tests), "tests.")
		print("goodbye.")

class Main():
	def main():
		tester = CubeSimTests()
		tests = [tester.test_orient_cube1, tester.test_orient_cube2, tester.test_orient_cube3]
		tester.run_tests(tests)

	if __name__ == "__main__":
		main()
