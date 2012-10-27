from string import printable
from random import randint


class Generator(object):
    def __init__(self, predicates, shortest=None, longest=None,
            all_possible=None):
        self.VALID, self.INVALID = self._get(predicates, options=all_possible)
        self.SHORTEST = -1 if shortest is None else shortest
        self.LONGEST = -1 if longest is None else longest
        
    def valid(self):
        length = randint(max(0, self.shortest), min(longest, int().max()))
        r = ""
        while len(r) < length:
            r += self.VALID_CHARS[randint(0, len(self.VALID))]

        return r

    def invalid(self):
        length = [randint(self.LONGEST + 1, int().max()), randint(0, max(self.SHORTEST - 1, 0))][randint(0,1)]
        r = ""
        while len(r) < length:
            r += self.INVALID[randint(0, len(self.INVALID))]

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
