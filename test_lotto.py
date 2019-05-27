import unittest
from lotto import Lotto

class TestLotto(unittest.TestCase):

    def test_lotto_can_initiate(self):
        Lotto()

    def test_lotto_can_initiate_with_parameters(self):
        Lotto(n=5, k=3, j=3, l=2)

    def test_lotto_can_display_numbers(self):
        l = Lotto(n=5)
        self.assertEqual(l.numbers(), set([1,2,3,4,5]))
