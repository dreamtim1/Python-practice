a, b, act = input(), input(), input()
try:
    print(eval('('+a+')' + {'mod': '%', 'div': '//', 'pow': '**'}.get(act, act) + b))
except ZeroDivisionError:
    print('Деление на 0!')
