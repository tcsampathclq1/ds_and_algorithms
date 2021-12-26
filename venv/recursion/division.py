def division_quotient(num, den):
    if num < 1 or den < 1:
        return 0
    if num - den < 0:
        return 0

    return 1 + division_quotient(num-den, den)

def division_remainder(num, den):
    if num < 1 or den < 1:
        return 0
    if num < den:
        return num
    elif num == den:
        return 0

    return division_remainder(num - den, den)


def main():
    quotient = division_quotient(24, 5)
    print(quotient)
    remainder  = division_remainder(10, 3)
    print(remainder)


if __name__ == "__main__":
    main()