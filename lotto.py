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
        c1 = frozenset([3,2,1])
        c2 = frozenset([1,2,4])
        c3 = frozenset([1,2,5])
        c4 = frozenset([1,3,4])
        c5 = frozenset([1,3,5])
        c6 = frozenset([1,4,5])
        c7 = frozenset([2,3,4])
        c8 = frozenset([2,3,5])
        c9 = frozenset([2,4,5])
        c10 = frozenset([3,4,5])
        return set([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])
        
