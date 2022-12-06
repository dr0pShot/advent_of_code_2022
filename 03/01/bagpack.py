f = open('input.txt', 'r')
lines = f.readlines()
letters_lower = 'abcdefghijklmnopqrstuvwxyz'
letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
points = 0
for line in lines:
    line = line.strip('\n')
    first, second = line[:len(line)//2], line[len(line)//2:]
    matches = []
    for i in range(len(first)):
        if first[i] in second and first[i] not in matches:
            matches.append(first[i])
    for i in range(len(letters_lower)):
        if letters_lower[i] in matches:
            points += i +1
    for i in range(len(letters_upper)):
        if letters_upper[i] in matches:
            points += i + len(letters_lower) + 1
print(points)