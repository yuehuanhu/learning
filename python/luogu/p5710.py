s = int(input())
s1 = s % 2 == 0
s2 = s > 4 and s <= 12
a = s1 and s2
Uim = s1 or s2
b = (s1 and not s2) or (not s1 and s2)
z = not s1 and not s2
answer = ""
for i in [a, Uim, b, z]:
    if i == True:
        answer = answer + "1 "
    elif i == False:
        answer = answer + "0 "
print(answer)
