def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    s: int = int(input())
    an: int = fibonacci(s)
    print(an)


if __name__ == "__main__":
    main()
