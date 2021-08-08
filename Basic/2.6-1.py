res = 0
s = 0
while True:
    a = int(input())
    s += a
    res += a ** 2
    if s == 0:
        break

print(res)
