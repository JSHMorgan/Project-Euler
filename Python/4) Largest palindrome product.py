def main() -> object:
    biggest_number: int = 0
    temp: int = 0

    # This iterates through every sum of three digit numbers to find the biggest palindrome.
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if (i * j) > biggest_number and is_palindrome(i * j):
                biggest_number = i * j

    print(biggest_number)


def is_palindrome(palindrome: object) -> object:
    """
        Function to find the palindrome of a string (as reversed only works on strings).
        Converts every object into a string when needed.
        :rtype: boolean
    """
    reverse_palindrome = ''.join(reversed(str(palindrome)))

    if str(palindrome) == reverse_palindrome:
        return True
    return False


main()
