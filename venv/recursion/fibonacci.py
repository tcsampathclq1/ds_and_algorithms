def fibonacci(num):
    if num < 0:
        return 0
    elif num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    res = fibonacci(8)
    print(res)


if __name__ == "__main__":
    main()