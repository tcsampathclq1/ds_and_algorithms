def exponent(base, power):
    if base == 0 or base == 1 or power == 0:
        return 1

    return base * exponent(base, power-1)

def main():
    res = exponent(9, 5)
    print(res)


if __name__ == "__main__":
    main()