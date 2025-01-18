s = input()
if s[-1] == "\r":
    s = s[:-1]
print(s[::-1])
