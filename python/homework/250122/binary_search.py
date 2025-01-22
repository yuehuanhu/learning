from typing import List


def binary_search(n: int, L: List[int]):
    start: int = 0
    end: int = len(L) - 1
    mid: int = (end - start) // 2
    while n != L[mid]:
        if start >= end:
            return False
        if n < L[mid]:
            end = mid - 1
            mid = (end + start) // 2
        else:
            start = mid + 1
            mid = (end + start) // 2
    return mid


def main() -> None:
    s0: str = input("请输入待查找数据")
    s1: List = input("请输入数组").split()
    n: int = int(s0)
    l: List[int] = list(map(int, s1))
    print(binary_search(n, l))


if __name__ == "__main__":
    main()
