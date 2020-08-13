from utils.YamlUtil import yml


class Testyaml:
    def test_load(self):
        s=yml.load_yaml('1.yml')
        print(s)
        print(type(s))

    def test_dump(self):
        yml.dump_yaml('1.yml',{'a':1})
