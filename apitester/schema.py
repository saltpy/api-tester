class Schema(object):
    def __init__(self, predicates):
        self.fields = dict()
        for p in predicates:
            self.fields[p] = None

    def add(self, value):
        for predicate in self.fields.iterkeys():
            if predicate(value):
                self.fields[predicate] = value

    def build(self):
        mapping = {}
        for pred, field in self.fields.iteritems():
            if field is not None:
                mapping[self._re_case(str(pred))] = field
        
        return mapping

    def _re_case(self, funcname):
        s = ''
        for token in funcname.split(' ')[1].split('_'):
            chars = list(token)
            chars[0] = chars[0].upper()
            s += ''.join(chars)

        return s

