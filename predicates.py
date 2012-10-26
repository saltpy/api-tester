from re import search

def is_always_a_match(v):
    return True

def is_always_a_mismatch(v):
    return False

def is_matching(v, regex):
    return search(regex, v) is not None

def is_at_least_as_long_as(v, n):
    return is_at_least(len(v), n)

def is_at_least_as_short_as(v, n):
    return is_at_most(len(v), n)

def is_at_least(v, n):
    return v >= n

def is_at_most(v, n):
    return v <= n

def is_exactly(v, ov):
    return v == ov

def is_in(v, vs):
    return v in vs

def is_a_kind_of(v, ov):
    return isinstance(v, ov) or issubclass(v, ov)
