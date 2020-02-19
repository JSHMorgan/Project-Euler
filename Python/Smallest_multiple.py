def main():
    counter: int = 0

    for i in range(2520, 999999999, 20):
        for j in range(11, 20):
            if i % j == 0:
                counter += 1
            else:
                break

        if counter == 9:
            print("yes {0}".format(i))
            break
        else:
            print("no {0}".format(i))
            counter = 0


main()