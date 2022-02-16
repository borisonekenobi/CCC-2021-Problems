def largestSquare(x, y, yard):
    for i in range(0, len(yard)):
        if i + x >= len(yard) or i + y >= len(yard):
            return i - 1
        for j in range(x, x + i):
            for k in range(y, y + i):
                if yard[j][k] == 1:
                    return i - 1
                    

N = int(input())
yard = []
for i in range(0, N):
    yard.append([0]*N)
T = int(input())
for i in range(0, T):
    location = input().split(' ')
    R = int(location[0]) - 1
    C = int(location[1]) - 1
    yard[R][C] = 1
largestPool = 0

for i in range(0, N - 1):
    for j in range(0, N - 1):
        largestPool = max(largestPool, largestSquare(i, j, yard))
print(largestPool)