instructions = list(input())
notes = ''
direction = ''
amount = 0
for i in range(0, len(instructions)):
    if instructions[i] in ('ABCDEFGHIJKLMNOPQRST'):
        notes = notes + instructions[i]
    elif instructions[i] == '+':
        direction = 'tighten'
    elif instructions[i] == '-':
        direction = 'loosen'
    else:
        amount = amount*10 + int(instructions[i])
        if i == len(instructions) - 1 or instructions[i+1] in ('ABCDEFGHIJKLMNOPQRST'):
            print(notes, direction, amount)
            notes = ''
            direction = ''
            amount = 0