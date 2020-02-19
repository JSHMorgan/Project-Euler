from typing import List


def main() -> object:
    multiples: List[int] = []
    total: int = 0

    for i in range(1, 1000):
        if i % 5 == 0 or i % 3 == 0:
            print(i)
            total += i

    print(total)


main()
