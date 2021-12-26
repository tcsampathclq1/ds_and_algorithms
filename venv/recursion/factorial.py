def factorial(num):
    if num <= 0:
        return 1

    return num * factorial(num-1)

def main():
    res = factorial(-1)
    print(res)


if __name__ == "__main__":
    main()