from apitester import Schema, Runner, is_always_a_match


def merchant_ref(v):
    return is_always_a_match(v)


def no_invalid_test():
    s = Schema([is_always_a_match])
    s.add('passing mref')
    r = Runner(s, "http://httpbin.org/post")
    r.run()


def one_invalid_test():
    s = Schema([is_always_a_match])
    s.add('passing_mref')
    r = Runner(s, "http://httpbin.org/post", invalid={'MerchantRef': None})
    r.run()


if __name__ == '__main__':
    no_invalid_test()
    one_invalid_test()
