N = int(input())
starPlayers = 0
for i in range(0, N):
    P = int(input()) * 5
    F = int(input()) * 3
    if P - F > 40:
        starPlayers+=1
if starPlayers == N:
    print(str(N) + '+')
else:
    print(starPlayers)