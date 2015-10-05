import unittest
#find the maximum of three numbers
def max3(x,y,z):
	if x >= y and x >= z:
		return x
	elif y >= x and y >= z:
		return y
	elif z >= x and z >= y:
		return z

class Max3Tester(unittest.TestCase):
	def test_1(self):
		self.assertEquals(max3(1,2,3), 3)

	def test_2(self):
		self.assertEquals(max3(30,20,10), 30)

	def test_3(self):
		self.assertEquals(max3(4,6,5), 6)

	def test_4(self):
		self.assertEquals(max3(2,2,1), 2)

if __name__=="__main__":
	unittest.main(verbosity=2)