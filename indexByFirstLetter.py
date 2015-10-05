import unittest

def indexByFirstLetter(listOfStrings):
	d = {}
	for word in listOfStrings:
		if word[0] in d:
			d[word[0]].append(word)
		else:
			d[word[0]] = [word]
	return d


class FirstLetterIndexTester(unittest.TestCase):
	def test_1(self):
		words = ["box", "able", "acorn", "barrel", "cat"]
		result = indexByFirstLetter(words)

		self.assertEquals(result["a"], ["able", "acorn"])
		self.assertEquals(result["b"], ["box", "barrel"])
		self.assertEquals(result["c"], ["cat"])


if __name__=="__main__":
	unittest.main(verbosity=2)