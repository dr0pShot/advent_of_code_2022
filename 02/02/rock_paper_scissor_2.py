# A Rock B Paper C Scissor
# X Loose | Y Draw | Z Win

def match_points(opponent, me):
    my_moves = [1, 2, 3]
    move = 0
    if opponent == 'A':
        move = 0
    if opponent == 'B':
        move = 1
    if opponent == 'C':
        move = 2
    if me == 'X':
        move -= 1
        return my_moves[move % 3]
    if me == 'Y':
        return 3 + my_moves[move % 3]
    if me == 'Z':
        move += 1
        return 6 + my_moves[move % 3]

f = open('input.txt', 'r')
lines = f.readlines()
current_points = 0
for line in lines:
    opponent, me = line.strip('\n').split(' ')
    current_points += match_points(opponent, me)
print(current_points)