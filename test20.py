import unittest
import 20

class MyTests(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(20.BastShoe('1 Привет'), 'Привет')
        self.assertEqual(20.BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(20.BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(20.BastShoe('3 0'), 'П')
        self.assertEqual(20.BastShoe('3 1'), 'р')
        self.assertEqual(20.BastShoe('3 2'), 'и')
        self.assertEqual(20.BastShoe('3 3'), 'в')
        self.assertEqual(20.BastShoe('3 100'), '')

if __name__ == '__main__':
    unittest.main()
