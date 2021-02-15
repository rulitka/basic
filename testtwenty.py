import unittest
import twenty

class MyTests(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(twenty.BastShoe('1 Привет'), 'Привет')
        self.assertEqual(twenty.BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('3 0'), 'П')
        self.assertEqual(twenty.BastShoe('3 1'), 'р')
        self.assertEqual(twenty.BastShoe('3 2'), 'и')
        self.assertEqual(twenty.BastShoe('3 3'), 'в')
        self.assertEqual(twenty.BastShoe('3 100'), '')

if __name__ == '__main__':
    unittest.main()
