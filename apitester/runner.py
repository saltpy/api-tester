from requests import post


class Runner(object):
    def __init__(self, schema, url, invalid=None):
        self.url = url
        self.invalid = {} if invalid is None else invalid
        self.expected = []
        self.actual = []
        self.response = None
        self.payload = schema.build()

        for field, value in self.invalid.iteritems():
            self.payload[field] = value
            self.expected.append((field, value))

    def run(self):
        self.response = post(self.url, data=self.payload)
        self._get_facts()
        self._report()

    def _get_facts(self):
        self.actual = []

    def _report(self):
        print "-" * 80
        print "PASS:" if self.actual == self.expected else "FAIL:"
        print "\targs=%s\n\tresponse=%s\n" %(self.payload, self.response) 
        for fact in self.actual:
            if fact not in self.expected:
                print "Mismatch on %s" %(fact,)
