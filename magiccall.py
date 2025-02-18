class Meta_1(type):
    def __call__(cls, *a, **kw):
        print('entering Meta_1.__call__()')
        rv = super().__call__(*a, **kw)
        print('exiting Meta_1.__call__()')
        return rv


class Class_1(metaclass=Meta_1):
    def __new__(cls, *a, **kw):
        print('entering Class_1.__new__()')
        rv = super().__new__(cls, *a, **kw)
        print('exiting Class_1.__new__()')
        return rv

    def __init__(self, *a, **kw):
        print('executing Class_1.__init__()')
        super().__init__(*a, **kw)


def main():
    c = Class_1()


if __name__ == '__main__':
    main()
