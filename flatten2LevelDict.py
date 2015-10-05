import unittest

def flatten2LevelDict(x):
	result = {}
	for key in x.keys():
		for i in x[key]:
			result[(key, i)] = x[key][i]
	return result 

class Flatten2LevelDictTester(unittest.TestCase):
	def test_1(self):
		x = {}
		x["a"] = {"A": 1, "B": 10}
		x["b"] = {"C": 15, "A": 3}

		result = flatten2LevelDict(x)

		self.assertEquals(result[("a", "A")], 1)
		self.assertEquals(result[("a", "B")], 10)
		self.assertEquals(result[("b", "C")], 15)
		self.assertEquals(result[("b", "A")], 3)

if __name__=="__main__":
	unittest.main(verbosity=2)