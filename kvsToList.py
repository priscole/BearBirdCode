import unittest

def kvsToList(aString):
	split1 = aString.split(",")
	two = []
	for i in split1:
		two.append(tuple(i.split("=")))
	return two 



class KVsToListTester(unittest.TestCase):
	def test_1(self):
		result = kvsToList("name=bird,email=bird@gmail,address=22-04")
		expected = [
			("name", "bird"),
			("email", "bird@gmail"),
			("address", "22-04")]
		self.assertEquals(result, expected)

if __name__=="__main__":
	unittest.main(verbosity=2)