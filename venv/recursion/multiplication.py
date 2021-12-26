def multiply(a, b):
    if a == 0 or b <= 0:
        return 0
    elif b == 1:
        return a

    return a + multiply(a, b-1)


def main():
    res = multiply(8, 5)
    print(res)


if __name__ == "__main__":
    main()