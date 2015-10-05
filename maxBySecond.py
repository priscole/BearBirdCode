import unittest

def maxBySecondField(items):
	maxRun = None
	alpha = None
	for item in items:
		if item[1] > maxRun:
			maxRun = item[1]
			alpha = item[0]
	return (alpha, maxRun)
		


class MaxBySecondFieldTester(unittest.TestCase):
	def test_1(self):
		items = [('a', 10), ('b', 1), ('c', 100), ('d', 2)]
		result = maxBySecondField(items)
		self.assertEquals(result, ('c', 100))

	def test_2(self):
		items = [("a", 10), ("b", 100), ("c", 1), ("d", 2)]
		result = maxBySecondField(items)
		self.assertEquals(result, ('b', 100))

	def test_3(self):
		items = [("A", -1)]
		result = maxBySecondField(items)
		self.assertEquals(result, ('A', -1))

if __name__=="__main__":
	unittest.main(verbosity=2)