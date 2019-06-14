from itertools import combinations
from random import randint

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
        # psychic promises at least j items are correct within n:
        # generate all possible winning combinations (n choose j).
        for combination in combinations(self._set, self._j):
            # use frozenset because it is hashable and can be placed in a set.
            # use set/frozenset because we care about set equality 
            # not tuple equality.
            # also, we can use a frozenset as a dictionary key.
            s.add(frozenset(combination))
        return s

    def possibilities_fully_covered(self, ticket_set):
        # after generating hashmap of all possible winning combinations (pwc), 
        # set each possible winning combination as False 
        # (False means this pwc is not 'covered' by any ticket)
        pwc_covered = {}
        for combination in self.possible_winning_number_combinations():
            pwc_covered[combination] = False

        # for each ticket in set of tickets presented to us
        for ticket in ticket_set:
            # generate all pwcs covered by this ticket
            covered_pwcs = self._generate_covered_pwcs(ticket)
            # mark each covered possibility in hashmap as True
            for i in covered_pwcs:
                pwc_covered[i] = True

        # loop through to check if any of the pwcs is not covered
        for key,value in pwc_covered.items():
            if (value == False):
                return False
        return True


    # assume l items within ticket's k slots is a winning combination
    def _generate_covered_pwcs(self, ticket):
        covered_pwcs = set()
        # each ticket has k slots, but only l are needed to 'win'
        # generate all winning combinations involving l items (k choose l)
        for l_combination in combinations(ticket, self._l):
            # within each l_combination, the remaining slots (k - l) can be filled
            # with any unused number and that is still a valid pwc
            pwc = frozenset(l_combination) # for set difference
            # remove pwc from n
            unused_numbers = self._set - pwc
            remaining_combinations = combinations(unused_numbers, self._k - self._l)
            # generate all winning pwc for this combination of l
            # by combining l combination with every remaining combinations
            for remaining_combination in remaining_combinations:
                s = set(l_combination).union(set(remaining_combination))
                covered_pwcs.add(frozenset(s))
        return covered_pwcs

    def generate_minimum_tickets_needed(self):
        # use a randomised algorithm (suggested by book) to generate tickets 
        # until all possible winnning combinations are covered
        tickets = set()
        possibilities = list(combinations(self._set, self._k))
        while not (self.possibilities_fully_covered(tickets)):
            random_possibility = frozenset(possibilities[randint(0, len(possibilities) - 1)])
            tickets.add(random_possibility)
        return tickets
