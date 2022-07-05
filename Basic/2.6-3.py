lst, x = [int(el) for el in input().split()], int(input())
print(' '.join(map(str, [i for i in range(len(lst)) if lst[i] == x])) if x in lst else 'Отсутствует')
