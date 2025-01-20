s = input().split("-")
x = s[0] + s[1] + s[2]
t = 0
for i in range(9):
    t = t + int(x[i]) * (i + 1)
answer = t % 11
if answer == 10:
    answer = "X"
if str(answer) == s[3]:
    print("Right")
else:
    print(s[0] + "-" + s[1] + "-" + s[2] + "-" + str(answer))
