import unittest

def function(a, b):
    a += 1
    return a + b

class MyTests(unittest.TestCase):

    def test_one(self):
        a = 5
        b = 6
        result = function(a, b)
        self.assertEqual(result, 12)
        self.assertEqual(a, 6)

if __name__ == '__main__':
    unittest.main()
