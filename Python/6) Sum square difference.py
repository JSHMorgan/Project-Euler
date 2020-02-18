import math


def main():
    sum_of_squares: int = 0
    square_of_sum: int = 0
    difference: int = 0

    for i in range(101):
        sum_of_squares += int(math.pow(i, 2))
        square_of_sum += i

    square_of_sum = int(math.pow(square_of_sum, 2))
    difference = square_of_sum - sum_of_squares

    print(difference)


main()
