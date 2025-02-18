from dataclasses import dataclass
from collections import deque

@dataclass
class Data:
    example: str


def main():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)

    d = Data(3)
    print(d.example)


    queue = deque(["Eric", "John", "Michael"])
    queue.append("Graham")                          # Graham arrives
    print(queue.popleft())                          # The first to arrive now leaves
    print(queue.popleft())                          # The second to arrive now leaves
    print(queue)                                    # Remaining queue in order of arrival

    print([x**2 for x in range(10)])


    a = [1, 2 , 3]
    b = [1, 3, 3]
    print(a == b)

if __name__ == "__main__":
    main()
