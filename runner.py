class Runner(object):
    def __init__(self, form, url, dest, invalid=None):
        self.invalid = {} if invalid is None else invalid
        self.xml = ElementTree.fromstring(form)
        self.expected = []
        self.facts = []
        self.response = ""

        for field, value in self.invalid.iteritems():
            el = xml.findall(field)[0]
            el.text = value
            self.expected += ["%s: Invalid"]

        self._run()
        self._get_facts()
        self._report()

    def _run(self):
        self.response = ""

    def _get_facts(self):
        pass

    def report(self):
        if self.facts == self.expected:
            print "Test Passed."
        else:
            print "Test Failed:"
            print "-" * 80
            for fact in self.facts:
                if fact not in self.expected:
                    print "Mismatch: %s was not returned" %(fact)
            print "-" * 80

