def Fib(n):
    L = [0, 1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(3, n + 1):
            L.append(L[0] + L[1])
            L.pop(0)
        return L[1]


s = int(input())
an = Fib(s)
print(an)
