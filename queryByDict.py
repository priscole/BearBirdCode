import unittest

def queryByDict(queryDict, listOfDicts):
	for d in listOfDicts:
		for k in queryDict:
			if d[k] == queryDict[k]:
				return dict 

class QueryByDictTester(unittest.TestCase):
	def test_1(self):
		items = [
		{'species': "elliptio", "maturity": "adult", "size": "big","id": 453},
		{'species': "elliptio", "maturity": "adult", "size": "small","id": 67},
		{'species': "corby", "maturity": "infant", "size": "small","id": 107},
		{'species': "elliptio", "maturity": "adult", "size": "big","id": 23}
		]

		q1 = {'species': 'elliptio'}
		result = queryByDict(q1, items)
		expected = [
			{'species': "elliptio", "maturity": "adult", "size": "big","id": 453},
			{'species': "elliptio", "maturity": "adult", "size": "small","id": 67},
			{'species': "elliptio", "maturity": "adult", "size": "big","id": 23}
		]
		self.assertEquals(result, expected)

		q2 = {'species': 'elliptio', "size": "big"}
		result = queryByDict(q2, items)
		expected = [
			{'species': "elliptio", "maturity": "adult", "size": "big","id": 453},
			{'species': "elliptio", "maturity": "adult", "size": "big","id": 23}
		]
		self.assertEquals(result, expected)

		q3 = {"id": 107}
		result = queryByDict(q3, items)
		expected = [{'species': "corby", "maturity": "infant", "size": "small","id": 107},]
		self.assertEquals(result, expected)

if __name__=="__main__":
	unittest.main(verbosity=2)