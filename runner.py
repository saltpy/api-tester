class Runner(object):
    def __init__(self, schema, url, invalid=None):
        self.invalid = {} if invalid is None else invalid
        self.expected = []
        self.actual = []
        self.response = None
        self.payload = schema.payload()

        for field, value in self.invalid.iteritems():
            self.payload[field] = value
            self.expected.append((field, value))

    def run(self):
        self.response = post(url, data=self.payload)
        self._get_facts()
        self._report()

    def _get_facts(self):
        print self.response
        self.actual = []

    def _report(self):
        if self.actual == self.expected:
            print "Test Passed."
        else:
            print "Test Failed:"
            print "-" * 80
            for fact in self.actual:
                if fact not in self.expected:
                    print "Mismatch: %s was not returned" %(fact)
            print "-" * 80

