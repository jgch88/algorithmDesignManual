from itertools import combinations

class Lotto:
    """
    A Lotto class based on Steven Skiena's Algorithm Design Manual (Chapter 1)
    """
    def __init__(self, n=15, k=6, j=4, l=3):
        self._n = n
        self._k = k # slots on ticket
        self._j = j # number of psychically-promised correct numbers in n
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
        for i in combinations(self._set, self._j):
            # frozenset so that it is hashable and can be placed in a set
            # set allows equality of elements without order, unlike tuples
            s.add(frozenset(i))
        return s

    def possibilities_fully_covered(self, ticket_set):
        # generate hashmap of all possible winning combinations, setting each 
        # combination as False (means this possibility is uncovered)
        h = {}
        for c in self.possible_winning_number_combinations():
            h[c] = False

        # for each ticket
        # generate covered possibilities (k choose l)
        for ticket in ticket_set:
            covered = self._generate_covered_possibilities(ticket)
            # mark each covered possibility in hashmap as True
            for i in covered:
                h[i] = True
        for key,value in h.items():
            if (value == False):
                print(key, value)
                return False
        return True

    def _generate_covered_possibilities(self, ticket):
        # each ticket, e.g. {1,2,4} covers {1,2,*}, {1,4,*}, {2,4,*}
        # or (k choose l) * ((n - l) choose (k - l)) possibilities
        # e.g. {1,2,*} covers {1,2,3}, {1,2,4}, {1,2,5}
        # {1,4,*} covers {1,4,2} (same as {1,2,4} above), {1,4,3}, {1,4,5}
        # (2,4,*} covers {2,4,1} (overlap), {2,4,3}, {2,4,5}
        covered = set()
        for possible_winning_combination in combinations(ticket, self._l):
            pwc = frozenset(possible_winning_combination)
            # remove pwc from n
            remaining_numbers = self._set - pwc
            # in the simple example, there's only 3 remaining numbers because
            # there's only one slot left.
            # in the second test case, there are 12 remaining numbers
            # but we can't just append to the pwc set, because there will only be 4 numbers out of k=6 slots. we need to union all possible 12 choose 3 combinations
            # to flag every lottery draw possibility covered by this ticket.
            # i.e. generate all the *s in {10,13,14,*,*,*}
            remaining_combinations = combinations(remaining_numbers, self._k - self._l)
            print('pwc', pwc, 'ticket', ticket)

            # generate all permutations using this pwc
            # for combination in remaining_combinations
            for combination in remaining_combinations:
                s = set(possible_winning_combination)
                s2 = set(combination)
                # union a remaining combination until no remaining combinations are left
                fs = s.union(s2)
                print(fs)
                # add permutations to covered set
                covered.add(frozenset(fs))
        return covered

