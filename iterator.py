class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def main():
    print("main function")
    test_str = "golf"
    for ch in Reverse(test_str):
        print(ch)


if __name__ == "__main__":
    main()
