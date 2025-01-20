def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def main():
    s = int(input())
    print(fact(s))


if __name__ == "__main__":
    main()
