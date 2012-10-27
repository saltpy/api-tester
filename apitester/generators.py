from string import printable
from random import randint


class Generator(object):
    def __init__(self, predicates, shortest, longest, all_possible=None):
        self.VALID, self.INVALID = self._get(predicates, options=all_possible)
        self.SHORTEST = -1 if shortest is None else shortest
        self.LONGEST = -1 if longest is None else longest
        
    def valid(self):
        length = randint(self.SHORTEST, self.LONGEST)
        r = ""
        while len(r) < length:
            r = r + self.VALID[randint(0, len(self.VALID) - 1)]

        return r

    def invalid(self):
        if self.SHORTEST is 0:
            l_index = 1
        else:
            l_index = randint(0,1)
        length = [randint(self.LONGEST + 1, self.LONGEST + 10),
                randint(0, min(self.SHORTEST - 1, 9))][l_index]
        r = ""
        while len(r) < length:
            r = r + self.INVALID[randint(0, len(self.INVALID) - 1)]

        return r

    def _get(self, predicates, options=None):
        v = []
        iv = []
        for c in options if options is not None else printable:
            add = True
            for predicate in predicates:
                if not predicate(c):
                    iv.append(c)
                    add = False
                    break
            if add:
                v.append(c)

        return (v, iv)
