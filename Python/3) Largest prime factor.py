import math


def main():
    number: int = 600851475143
    for i in range(math.isqrt(number), 2, -1):
        if is_prime(i) and number % i == 0:
            print(i)
            break


def is_prime(number: int):
    for i in range(2, math.isqrt(number)):
        if number % i == 0:
            return False
    return True


main()
