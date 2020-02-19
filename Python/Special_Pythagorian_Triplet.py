import math


def main():
    find_triplet_product: int = 0
    limit: int = 1000

    for a in range(1, limit):
        for b in range(a, limit):
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
            if c.is_integer() and a + b + c == 1000:
                c = int(c)
                print(f"{a} + {b} + {c} = 1000")
                print(f"{a * b * c}\n")


main()
