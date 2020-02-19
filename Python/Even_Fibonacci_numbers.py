from typing import List


def main() -> object:
    fibonacci_numbers: List[int] = [1, 2]
    total: int = 0
    while fibonacci_numbers[-1] < 4000000:
        fibonacci_numbers.append((fibonacci_numbers[-1] + fibonacci_numbers[-2]))

    for fibonacci_number in fibonacci_numbers:
        if fibonacci_number % 2 == 0:
            total += fibonacci_number

    print(total)


main()
