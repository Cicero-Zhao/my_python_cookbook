import ConfigParser


class FakeHeader(object):

    def __init__(self, fp, section='zconfig'):
        self.section = '[%s]\n' % section
        self.fp = fp

    def readline(self):
        if self.section:
            try:
                return self.section
            finally:
                self.section = None
        else:
            return self.fp.readline()


class ZConfigParser(ConfigParser.ConfigParser, object):

    def __init__(self, default_section='zconfig'):
        ConfigParser.ConfigParser.__init__(self)
        self.default_section = default_section

    def read(self, fp):
        new_fp = FakeHeader(open(fp), self.default_section)
        return super(ZConfigParser, self).readfp(new_fp)

    def write(self, fp):
        fp = open(fp, "w")
        for (key, value) in self.items(self.default_section):
            fp.write("%s = %s\n" % (key, str(value).replace('\n', '\n\t')))
        fp.write("\n")

    def get(self, key):
        return super(ZConfigParser, self).get(self.default_section, key)

    def set(self, key, value):
        super(ZConfigParser, self).set(self.default_section, key, value)


zconfig = ZConfigParser()
zconfig.read("test2.cfg")

print zconfig.get('key1')

zconfig.set('key1', 'alfasjdlfabalalla')

zconfig.write('test3.cfg')

