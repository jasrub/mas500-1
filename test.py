import MC_HW1intermediate
import unittest

class TestMediaCloudAPICall (unittest.TestCase):
	def testMediaCloudAPICall (self):
		res = MC_HW1intermediate.call_media_cloud()
		assert res!=None

if __name__ == "__main__":
    unittest.main()