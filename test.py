#import pytest
from code import lambda_dep as j
import unittest

class Testj(unittest.TestCase):
    def test_ad(self):
       
        a = 10
        b = 20
        result = j.ad(a,b)
        self.assertEqual(result, 30)

    def test_ad_neg(self):
        a = 20
        b = 10
        result = j.ad(a,b)
        self.assertEqual(result, 10)
if __name__ == '__main__':
    unittest.main()

"""
@pytest.fixture
def input_value():
   a = 10
   b = 20
   x = 20
   y = 10
   return a,b,x,y

def test_ad():

    res = ad(a,b)
    assert res == 30

def test_ng():
    res = ad(x,y)
    assert res == 10

"""