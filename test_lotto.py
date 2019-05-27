import unittest
from lotto import Lotto

class TestLotto(unittest.TestCase):

    def test_lotto_can_initiate(self):
        Lotto()

    def test_lotto_can_initiate_with_parameters(self):
        Lotto(n=5, k=3, j=3, l=2)
