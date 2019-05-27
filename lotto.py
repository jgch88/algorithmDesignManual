from itertools import combinations

class Lotto:
    """
    A Lotto class based on Steven Skiena's Algorithm Design Manual (Chapter 1)
    """
    def __init__(self, n=15, k=6, j=4, l=3):
        self._n = n
        self._k = k
        self._j = j
        self._l = l
        self._set = self._generate_numbers();

    def numbers(self):
        return self._set

    def _generate_numbers(self):
        s = set()
        for i in range(1, self._n + 1):
            s.add(i)
        return s

    def possible_winning_number_combinations(self):
        s = set()
        for i in combinations(self._set, self._k):
            # frozenset so that it is hashable and can be placed in a set
            # set allows equality of elements without order, unlike tuples
            s.add(frozenset(i))
        return s

    def possibilities_fully_covered(self, ticket_set):
        return True
