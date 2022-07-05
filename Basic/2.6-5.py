def coordinate(k, size):
    if k == -1:
        return size - 1
    elif k == size:
        return 0
    else:
        return k
    
xs = 0
ys = 0
matrix = []
while True:
    s = input()
    if s == 'end':
        break
    lst = [int(el) for el in s.split()]
    if xs == 0:
        xs = len(lst)
    ys += 1
    matrix.append(lst)

result = []
for i in range(len(matrix)):
    result.append([])
    for j in range(len(matrix[i])):
        
        top = matrix[coordinate(i + 1, ys)][coordinate(j, xs)]
        bottom = matrix[coordinate(i - 1, ys)][coordinate(j, xs)]
        left = matrix[coordinate(i, ys)][coordinate(j - 1, xs)]
        right = matrix[coordinate(i, ys)][coordinate(j + 1, xs)]
        result[i].append(top + bottom + left + right)
        
for el in result:
    print(*el)
