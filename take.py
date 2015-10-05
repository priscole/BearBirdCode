import unittest

def take(n, items):
	newList = items[0:n]
	return newList


class TakeTester(unittest.TestCase):
	def test_1(self):
		result = take(2, ["a","b","c"])
		self.assertEquals(result, ["a", "b"])

	def test_2(self):
		result = take(0, [1,2,3])
		self.assertEquals(result, [])

	def test_3(self):
		result = take(5, ["a", "b", "c", "d"])
		self.assertEquals(result, ["a", "b", "c", "d"])

if __name__=="__main__":
	unittest.main(verbosity=2)