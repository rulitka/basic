import unittest
import twenty

class MyTests(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(twenty.BastShoe('1 Привет'), 'Привет')
        self.assertEqual(twenty.BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('4'), 'Привет')
        self.assertEqual(twenty.BastShoe('5'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('4'), 'Привет')
        self.assertEqual(twenty.BastShoe('5'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('5'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('5'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('5'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('4'), 'Привет')
        self.assertEqual(twenty.BastShoe('2 2'), 'Прив')
        self.assertEqual(twenty.BastShoe('4'), 'Привет')
        self.assertEqual(twenty.BastShoe('5'), 'Прив')
        self.assertEqual(twenty.BastShoe('5'), 'Прив')
        self.assertEqual(twenty.BastShoe('5'), 'Прив')

    def test_two(self):
        self.assertEqual(twenty.BastShoe('1 Привет'), 'Привет')
        self.assertEqual(twenty.BastShoe('1 , Мир!'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('1 ++'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('2 2'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!++')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('1 *'), 'Привет, Мир!*')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('4'), 'Привет, Мир!')
        self.assertEqual(twenty.BastShoe('3 6'), ',')
        self.assertEqual(twenty.BastShoe('2 100'), '')
       
    def test_three(self):
        self.assertEqual(twenty.BastShoe('1 a'), 'a')
        self.assertEqual(twenty.BastShoe('1 b'), 'ab')
        self.assertEqual(twenty.BastShoe('1 c'), 'abc')
        self.assertEqual(twenty.BastShoe('1 d'), 'abcd')
        self.assertEqual(twenty.BastShoe('1 e'), 'abcde')
        self.assertEqual(twenty.BastShoe('3 5'), '')

if __name__ == '__main__':
    unittest.main()
