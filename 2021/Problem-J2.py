N = int(input())
bids = []
for i in range(0, N):
    name = input()
    bid = int(input())
    bids.append([name, bid])

winner = bids[0][1]
for i in bids:
    winner = max(winner, i[1])
for i in bids:
    if winner == i[1]:
        print(i[0])