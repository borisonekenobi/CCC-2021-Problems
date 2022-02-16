instructions = []
while True:
    instructions.append(input())
    if instructions[-1] == 99999:
        break
instruct = []
previousDirection = ''
for i in range(0, len(instructions) - 1):
    direction = int(instructions[i] / 1000)
    steps = instructions[i] - (direction * 1000)
    direction = int(direction / 10) + int(direction - (int(direction / 10) * 10))
    if direction % 2 == 0 and direction != 0:
        instruct.append('right ' + str(steps))
        previousDirection = 'right '
    elif direction % 2 != 0:
        instruct.append('left ' + str(steps))
        previousDirection = 'left '
    else:
        instruct.append(previousDirection + str(steps))

print(instruct)