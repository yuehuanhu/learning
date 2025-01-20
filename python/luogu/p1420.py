s = input()
t = input().split()
n = 1
max = 1
for i in range(1, int(s)):
    if int(t[i]) == int(t[i - 1]) + 1:
        n = n + 1
        if n > max:
            max = n
    else:
        n = 1
print(max)
