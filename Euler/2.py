n = int(input())
s = 0
i = 1
k = 2
while k <= n:
    if k % 2 == 1:
        new_k = i + k
        i = k
        k = new_k
        continue
    else:
        new_k = i + k
        i = k
        k = new_k
        s += i
print(s)
