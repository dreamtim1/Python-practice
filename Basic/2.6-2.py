n = int(input())
num = 1
k = 1
for i in range(n - 1):
    print(num, end = ' ')
    k -= 1
    if k == 0:
        num += 1
        k = num
if k == 0:
    print(num + 1)
else:
    print(num)
