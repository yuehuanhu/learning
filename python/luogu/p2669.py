s = int(input())
answer = 0
i = 1
x = 1
y = 1
for i in range(1, s + 1):
    if x <= y:
        answer = answer + y
    else:
        y = y + 1
        answer = answer + y
        x = 1
    x = x + 1
print(answer)
