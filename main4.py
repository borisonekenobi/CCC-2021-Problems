X = int(input())
together = []
for i in range(0, X):
    together.append(input().split(' '))
Y = int(input())
apart = []
for i in range(0, Y):
    apart.append(input().split(' '))
G = int(input())
groups = []
for i in range(0, G):
    groups.append(input().split(' '))

tViolations = 0
aViolations = 0
for i in groups:
    for j in together:
        if i[0] in j:
            if i[1] not in j and i[2] not in j:
                tViolations+=1
        elif i[1] in j:
            if i[0] not in j and i[2] not in j:
                tViolations+=1
        elif i[2] in j:
            if i[0] not in j and i[1] not in j:
                tViolations+=1
    for j in apart:
        if i[0] in j:
            if i[1] in j or i[2] in j:
                aViolations+=1
        elif i[1] in j:
            if i[0] in j or i[2] in j:
                aViolations+=1
        elif i[2] in j:
            if i[0] in j or i[1] in j:
                aViolations+=1
print(int(tViolations/2) + aViolations)