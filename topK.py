import unittest

def topK(n, items):
#sort numbers highest to lowest, then make new list of first n or [:n]
	items.sort()
	items.reverse()
	return items[:n]


class TopKTester(unittest.TestCase):
	def test_1(self):
		items = [60, 5, 4, 80, 90, 10, 57]

		result = topK(3, items)
		expected = [90, 80, 60]		
		self.assertEquals(result, expected)
		self.assertEquals(items, [60, 5, 4, 80, 90, 10, 57])

if __name__=="__main__":
	unittest.main(verbosity=2)