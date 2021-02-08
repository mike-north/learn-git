import unittest
from calc import add, sub 

class TestStringMethods(unittest.TestCase):

    def test_add_2arg(self):
        # Make sure 3 + 4 = 7
        self.assertEqual(add(3, 4), 7, 'adding three and four')
        # Make sure 3 + (-2) = 1
        self.assertEqual(add(3, -2), 1, 'adding three and negative two')
   
    def test_sub_2arg(self):
        # Make sure 4 - 3 = 1
        self.assertEqual(sub(4, 3), 1, 'subtracting three from four')
        # Make sure (-2) - 3 = -5
        self.assertEqual(sub(-2, 3), -5, 'subtracting three from negative two')

if __name__ == '__main__':
    unittest.main()