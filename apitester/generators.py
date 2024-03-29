from string import printable
from random import randint


class Generator(object):
    def __init__(self, predicates, shortest, longest, all_possible=None):
        self.VALID, self.INVALID = self._get(predicates, options=all_possible)
        self.SHORTEST = shortest
        self.LONGEST = longest

    def valid(self):
        length = randint(self.SHORTEST, self.LONGEST)
        r = []
        while len(r) < length:
            r.append(self.VALID[randint(0, len(self.VALID) - 1)])

        return "".join(r)

    def invalid(self):
        ivlengths = range(0, max(0, self.SHORTEST - 1)) + range(self.LONGEST + 1, self.LONGEST + 10)
        length = ivlengths[randint(0, len(ivlengths) - 1)]
        r = []
        while len(r) < length:
            r.append(self.INVALID[randint(0, len(self.INVALID) - 1)])

        return "".join(r)

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
