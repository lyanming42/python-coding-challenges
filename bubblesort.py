def bubble_sort(ary):
    n = len(ary)
    for i in range(n):
        for j in range(n - i - 1):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]


def main():
    print("Bubble sort")
    bubble_sort(ary)
    print(ary)

ary = [2, 1, 8, 10, 7, 100, 21, 6, 3]

if __name__ == '__main__':
    main()
