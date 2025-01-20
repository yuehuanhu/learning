from typing import List, Tuple


def calc_leap_year(x: int, y: int) -> Tuple[int, List[str]]:
    n: int = 0
    year: list = []
    for i in range(x, y + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            n = n + 1
            year.append(str(i))

    return n, year


def main() -> None:
    s: List[str] = input().split()
    num: int
    year: List[str]
    num, year = calc_leap_year(int(s[0]), int(s[1]))
    print(num)
    print(" ".join(year))


if __name__ == "__main__":
    main()
