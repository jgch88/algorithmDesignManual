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

    def test_lotto_can_display_all_possible_winning_number_combinations(self):
        l = Lotto(n=5, k=3, j=3, l=2)
        # since k = 3, we have (5 choose 3 = 10) possible combinations
        c1 = frozenset([1,2,3])
        c2 = frozenset([1,2,4])
        c3 = frozenset([1,2,5])
        c4 = frozenset([1,3,4])
        c5 = frozenset([1,3,5])
        c6 = frozenset([1,4,5])
        c7 = frozenset([2,3,4])
        c8 = frozenset([2,3,5])
        c9 = frozenset([2,4,5])
        c10 = frozenset([3,4,5])
        self.assertEqual(l.possible_winning_number_combinations(), 
            set([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]))

