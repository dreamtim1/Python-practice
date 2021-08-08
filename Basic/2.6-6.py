n = int(input())
matrix = [[0 for i in range(n)] for i in range(n)]

i, j, switch = 0, 0, 0
mi, mj = 0, 0
dict = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}

for k in range(1, n**2 + 1):

    i += mi
    j += mj
    matrix[i][j] = k

    move = switch % 4
    mi = dict[move][0]
    mj = dict[move][1]

    if i + mi >= n or j + mj >= n or i + mi < 0 or j + mj < 0:
        switch += 1
    elif matrix[i + mi][j + mj] != 0:
        switch += 1

    move = switch % 4
    mi = dict[move][0]
    mj = dict[move][1]

for el in matrix:
    print(*el)
