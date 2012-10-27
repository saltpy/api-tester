from __future__ import print_function
from requests import post


class Runner(object):
    def __init__(self, schema, url, invalid=None, report_manager=print):
        self.rm = report_manager
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
        self.rm("-" * 80)
        self.rm("PASS:") if self.actual == self.expected else self.rm("FAIL:")
        self.rm("\targs=" + str(self.payload))
        self.rm("\tresponse=" + str(self.response)) 
        for fact in self.actual:
            if fact not in self.expected:
                self.rm("Mismatch on " + str(fact))
