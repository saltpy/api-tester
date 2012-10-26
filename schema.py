from xml.etree import ElementTree


class Schema(object):
    def __init__(self, predicates):
        self.fields = dict()
        for p in predicates:
            self.fields[p] = None

    def add(self, value):
        for predicate in self.fields.iterkeys():
            if predicate(value):
                self.fields[predicate] = value

    def build_form(self, template):
        mapping = {}
        for pred, field in self.fields.iteritems():
            if field is not None:
                mapping[self._re_case(str(pred))] = field

        try:
            xml = ElementTree.parse(template)
        except IOError:
            xml = ElementTree.fromstring(template)

        for field, value in r.iteritems():
            el = xml.findall(field)[0]
            el.text = value

        return xml

    def _re_case(self, funcname):
        s = ''
        for token in funcname.split(' ')[1].split('_'):
            chars = list(token)
            chars[0] = chars[0].upper()
            s += ''.join(chars)

        return s

