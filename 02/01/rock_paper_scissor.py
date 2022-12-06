# A Rock B Paper C Scissor
# X "    Y "     Z "

def match_points(opponent, me):
    if opponent == 'A' and me == 'X' or opponent == 'B' and me == 'Y' or opponent == 'C' and me == 'Z':
        return 3
    elif opponent == 'A' and me == 'Y':
        return 6
    elif opponent == 'B' and me == 'Z':
        return 6
    elif opponent == 'C' and me == 'X':
        return 6
    else:
        return 0

def move_points(me):
    if me == 'X':
        return 1
    if me == 'Y':
        return 2
    if me == 'Z':
        return 3
    return 0

f = open('input.txt', 'r')
lines = f.readlines()
current_points = 0
for line in lines:
    opponent, me = line.strip('\n').split(' ')
    current_points += match_points(opponent, me)
    current_points += move_points(me)
print(current_points)