def exampleGenerator(lst):
    for item in lst:
        yield item

def infiniteLoopGenerator():
    num = 0
    while(True):
        yield num
        num += 1


def main():
    lst = [1, 2, 3]
    # for item in exampleGenerator(lst):
    #     print(item)

    print(exampleGenerator(lst))


    infiniteGenerator = infiniteLoopGenerator()

    print(infiniteGenerator)
    print(next(infiniteGenerator))

    print(next(infiniteGenerator))


if __name__ == "__main__":
    main()
