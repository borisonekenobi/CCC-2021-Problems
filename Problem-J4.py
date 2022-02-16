# get input
countL, countM, countS = 0, 0, 0
for i in books:
    if i == 'L': countL+=1
    if i == 'M': countM+=1
    if i == 'S': countS+=1
desired = []
for i in range(len(books)):
    if i < countL: desired.append('L')
    elif i < countM + countL: desired.append('M')
    else: desired.append('S')
LinM, LinS, MinL, MinS, SinL, SinM = 0, 0, 0, 0, 0, 0
for i in range(len(books)):
    if desired[i] == 'L' and books[i] == 'M': MinL+=1
    if desired[i] == 'L' and books[i] == 'S': SinL+=1
    if desired[i] == 'M' and books[i] == 'L': LinM+=1
    if desired[i] == 'M' and books[i] == 'S': SinM+=1
    if desired[i] == 'S' and books[i] == 'L': LinS+=1
    if desired[i] == 'S' and books[i] == 'M': MinS+=1

print(min(LinM, MinL) + min(MinS, SinM) + min(LinS, SinL) + ((abs(LinM - MinL) + abs(LinS - SinL) + abs(MinS - SinM)) / 3 * 2))