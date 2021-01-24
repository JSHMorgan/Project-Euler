import math


def main():
    limit: int = 10000000
    find_prime = 254368  # Change this number to find this numbered prime. E.g. the 3rd prime is 5.
    prime_sieve = sieve(limit)

    counter = 0
    for key, value in prime_sieve.items():
        if value:
            print(counter, ") ", key)
            counter += 1

        if counter == find_prime:
            print(key, "is the prime you are looking for.")
            break


def sieve(limit: int):
    prime_sieve = {
        2: True
    }

    for i in range(3, limit, 2):
        prime_sieve[i] = True

    for i in range(3, math.isqrt(i), 2):
        if prime_sieve[i]:
            counter = 0
            j = 0
            while j < limit:
                j = math.pow(i, 2) + (counter * i)
                prime_sieve[j] = False
                counter += 1

    return prime_sieve


if __name__ == "__main__":
    main()

