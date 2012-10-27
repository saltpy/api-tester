from apitester import Schema, Runner, is_exactly, Generator
from requests import get


def httpbin(*suffix):
    return "http://httpbin.org/" + '/'.join(suffix)


def one(v):
    return is_exactly(v, "1")


def one_valid_test():
    s = Schema([one])
    s.add(one_gen.valid())
    r = Runner(s, httpbin("post"))
    r.run()


def one_invalid_test():
    s = Schema([one])
    s.add(one_gen.valid())
    r = Runner(s, httpbin("post"), invalid={'One': one_gen.invalid()})
    r.run()


if __name__ == '__main__':
    r = get(httpbin("get"))
    # Test that httpbin is up
    assert r.status_code == 200

    one_gen = Generator([one], shortest=1, longest=1)
    one_valid_test()
    one_invalid_test()
