class Lotto:
    """
    A Lotto class based on Steven Skiena's Algorithm Design Manual (Chapter 1)
    """
    def __init__(self, n=15, k=6, j=4, l=3):
        self._n = n
        self._k = k
        self._j = j
        self._l = l
        self._set = self._generateNumbers();

    def numbers(self):
        return self._set

    def _generateNumbers(self):
        s = set()
        for i in range(1, self._n + 1):
            s.add(i)
        return s
        
