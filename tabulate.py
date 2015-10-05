import unittest

def tabulate(listofItems):
	d = {}
	for item in listofItems:
		if item in d:
			d[item] = d[item] + 1
		else:
			d[item] = 1
	return d
		

class TabulateTester(unittest.TestCase):
	def test_1(self):
		items = ["c", "a", "b", "b", "b", "c", "a", "d"]
		table = tabulate(items)
		self.assertEquals(table["c"], 2)
		self.assertEquals(table["a"], 2)
		self.assertEquals(table["b"], 3)
		self.assertEquals(table["d"], 1)

if __name__=="__main__":
	unittest.main(verbosity=2)