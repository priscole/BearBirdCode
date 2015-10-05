import unittest

def drop(n, items):
	if n < len(items):
		return items[n:]
	else:
	    return [] 

	

class DropTester(unittest.TestCase):
	def test_1(self):
		result = drop(2, ["a","b","c","d"])
		self.assertEquals(result, ["c", "d"])

	def test_2(self):
		result = drop(0, [1,2,3])
		self.assertEquals(result, [1,2,3])

	def test_3(self):
		result = drop(5, ["a", "b", "c", "d"])
		self.assertEquals(result, [])

if __name__=="__main__":
	unittest.main(verbosity=2)