def function_decorator(func):
    def wrapper():
        print("Before Calling")
        func()
        print("After Calling")
    return wrapper

@function_decorator
def example_func():
    print("func")

def add_id(cls):
    class WrapperCls(cls):
        def __init__(self, id, *kargs, **kwargs):
            super().__init__(*kargs, **kwargs)
            self._id = id

        def get_id(self):
            return self._id

    return WrapperCls

@add_id
class ExampleCls:
    pass

if __name__ == "__main__":
    example_func()
    example_cls = ExampleCls(3)
    print(example_cls.get_id())
