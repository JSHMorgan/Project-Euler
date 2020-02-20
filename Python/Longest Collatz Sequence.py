
def main():
    pass


if __name__ == "__main__":
    number: int = 1
    terms: int = 1
    temp: int = 0
    highest_current_terms = [0, 0]
    numbers = {
        number: terms
    }

    while number < 1000000:
        terms = 1
        temp = number
        while temp != 1:
            if temp not in numbers:
                terms += 1
                if temp % 2 == 0:
                    temp /= 2
                else:
                    temp = 3 * temp + 1
            else:
                terms += numbers[temp] - 1
                break

        numbers[number] = terms
        print(f"{number} : {terms}")
        if numbers[number] > highest_current_terms[1]:
            highest_current_terms[0] = number
            highest_current_terms[1] = terms
        number += 1

    print("Number with the highest terms in its sequence: ", end="")
    print(f"{highest_current_terms[0]}. Terms: {highest_current_terms[1]}")


main()
