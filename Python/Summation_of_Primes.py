from Ten_Thousand_and_first_prime import sieve


def main():
    limit: int = 2000000

    prime_sieve = sieve(limit)

    total: int = 0
    for key, value in prime_sieve.items():
        if value:
            total += key
    print(int(total))


main()
