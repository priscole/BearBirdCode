import unittest
import kvsToList

def kvsToDict(aString):
	# split1 = aString.split(",")
	d = {}
	# for i in split1:
	# 	d[i.split("=")[0]] = i.split("=")[1]
	# return d
	new = kvsToList.kvsToList(aString)
	for i in new:
		d[i[0]] = i[1]
	return d



class KVsToDictTester(unittest.TestCase):
	def test_1(self):
		result = kvsToDict("name=bird,email=bird@gmail,address=22-04")
		self.assertEquals(result["name"], "bird")
		self.assertEquals(result["email"], "bird@gmail")
		self.assertEquals(result["address"], "22-04")

if __name__=="__main__":
	unittest.main(verbosity=2)