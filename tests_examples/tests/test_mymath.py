import unittest

from tests_examples.mymath import add_ints

class TestMyMath(unittest.TestCase):
    def test_add_ints(self):
        """Test add_ints with a simple case"""
        self.assertEqual(add_ints(2, 3), 5)
        self.assertEqual(add_ints(-1, 1), 0)
        self.assertEqual(add_ints(0, 0), 0)

if __name__=='main':
    unittest.main()

# run from root dir
# python -m unittest tests_examples.tests.test_mymath
