import unittest
import tv_three

class MyTests(unittest.TestCase):
    #def setUp(self):


    def test_one(self):
        self.assertEqual(tv_three.MatrixTurn(["12", "34"], 2, 2, 1), (['31', '42']))

    def test_two(self):
        self.assertEqual(tv_three.MatrixTurn(["12", "34"], 2, 2, 2), (['43', '21']))

    def test_three(self):
        self.assertEqual(tv_three.MatrixTurn(["12", "34"], 2, 2, 3), (['24', '13']))
 
    def test_four(self):
        self.assertEqual(tv_three.MatrixTurn(["12", "34"], 2, 2, 4), (['12', '34']))

    def test_five(self):
        self.assertEqual(tv_three.MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 1), (['212345', '343456', '456767', '567898']))

    def test_six(self):
        self.assertEqual(tv_three.MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 2), (['321234', '454345', '567656', '678987']))
    
    def test_seven(self):
        self.assertEqual(tv_three.MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 3), (['432123', '565434', '676545', '789876']))
if __name__ == '__main__':
    unittest.main()
