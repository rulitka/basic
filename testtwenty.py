import unittest
import twenty

class MyTests(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(twenty.BastShoe('1 a'), 'a')
        self.assertEqual(twenty.BastShoe('1 b'), 'ab')
        self.assertEqual(twenty.BastShoe('1 c'), 'abc')
        self.assertEqual(twenty.BastShoe('1 d'), 'abcd')
        self.assertEqual(twenty.BastShoe('1 e'), 'abcde')
        self.assertEqual(twenty.BastShoe('3 5'), '')
        #self.assertEqual(twenty.BastShoe('4'), 'abcd')
        #self.assertEqual(twenty.BastShoe('5'), 'abcde')

if __name__ == '__main__':
    unittest.main()
