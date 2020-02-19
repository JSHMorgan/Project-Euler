from Ten_Thousand_and_first_prime import sieve
import math


limit: int = 75000
prime_list: int = []


def main():
    pass


def prime_factorisation(number):
    divisor_number: int = 1
    divided_num = number

    for i in range(len(prime_list)):
        # If there is a remainder left (as in, the divided number is not 0 when the next prime is bigger than its
        # square root) then since its exponent will be 1, and you add 1 to an exponent) you times number_of_divisors
        # by 2 to simulate this.
        if prime_list[i] > int(math.sqrt(number)):
            return divisor_number * 2

        # Reset the exponent for the current prime number and check if it is a prime factor of the number we are
        # testing by seeing if the number mod the prime is equal to 0. If that is the case then add one to the
        # exponent and half the number left after being divided.
        exponent = 0
        while divided_num % prime_list[i] == 0:
            exponent += 1
            divided_num /= prime_list[i]

        # The equation for finding divisors from prime factors requires you to add 1 to the exponents of each
        # prime factor therefore we times number_of_divisors by exponent + 1.
        divisor_number *= exponent + 1

        # Return number of divisors when there is no remainder after dividing by primes.
        if divided_num == 1:
            return divisor_number
    return divisor_number


def number_of_divisors(divisor_number):
    counter: int = 1  # Start at 2 divisors as every prime has at minimum 2 divisors.
    even_co_prime: int = 2
    odd_co_prime: int = 2
    divisors: int = 0

    if divisor_number == 1:
        return divisor_number, 1
    elif divisor_number == 2:
        return divisor_number, 2
    elif divisor_number == 3:
        return divisor_number, 4
    elif divisor_number == 4:
        return divisor_number, 6
    else:
        while divisors < divisor_number:
            if counter % 2 == 0:
                even_co_prime = prime_factorisation(counter + 1)
                divisors = even_co_prime * odd_co_prime
            else:
                odd_co_prime = prime_factorisation((counter + 1) / 2)
                divisors = even_co_prime * odd_co_prime
            counter += 1
        return int(counter * (counter - 1) / 2), divisors


if __name__ == "__main__":
    minimum_divisors: int = 500
    for key, value in sieve(limit).items():
        prime_list.append(key)
    divisible_num, divisor_num = number_of_divisors(minimum_divisors)
    print(f"{divisible_num} has {divisor_num} divisors which is the first amount of divisors over the minimum divisor "
          f"amount of {minimum_divisors}.")

main()
