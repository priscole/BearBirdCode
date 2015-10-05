import unittest

#adds together the numbers of like keys into a new dictionary
def addDicts(x, y):
	z = {}
	for key in x:
		if key in y:
			z[key] = x[key] + y[key]
		else: 
			z[key] = x[key]
	for key in y:
		if key not in x:
			z[key] = y[key]
	return z


class AddDictsTester(unittest.TestCase):
	def test_1(self):
		x = {"a": 1,  "b": 2, "c": 3}
		y = {"b": 20, "c": 30, "d": 40}
		result = addDicts(x,y)
		expected = {
		"a": 1,
		"b": 22,
		"c": 33,
		"d": 40
		}
		self.assertEquals(result, expected)

if __name__=="__main__":
	unittest.main(verbosity=2)