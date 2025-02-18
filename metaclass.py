class SingletoneMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        else:
            instance = cls._instances[cls]

        return instance

class SingletonClass(metaclass=SingletoneMeta):
    base_value = "Base Value"
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"BaseClass: value = {self.value}, base_value = {self.base_value}")


class DerivedClass(SingletonClass):
    derived_value = "Drived Value"

    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"DrivedClass: value = {self.value}, base_value = {self.derived_value}")

def main():
    obj = SingletonClass(3)
    obj.show()

    obj1 = SingletonClass(4)
    obj1.show()

    drivedObj = DerivedClass(3)
    drivedObj.show()

    drivedObj1 = DerivedClass(4)
    drivedObj1.show()

if __name__ == "__main__":
    main()
