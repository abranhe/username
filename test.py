import unittest
import username

class Test(unittest.TestCase):
	def test(self):
			self.assertTrue(len(username()) > 1)

if __name__ == '__main__':
    unittest.main()
