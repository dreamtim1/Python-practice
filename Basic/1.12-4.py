type = input()

a = int(input())
if type == 'круг':
    print(a**2 * 3.14)
elif type == 'прямоугольник':
    b = int(input())
    print(a * b)
else:
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
