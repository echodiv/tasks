class Singletone():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.foo = 'bar'


def test():
    class_one = Singletone()
    class_two = Singletone()
    assert class_one is class_two


if __name__ == '__main__':
    test()
