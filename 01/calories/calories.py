file = open('input.txt', 'r')
lines = file.readlines()
max = 0
current = 0
for l in lines:
    if len(l) == 1:
        if max < current:
            max = current
        current = 0
    else:
        current += int(l.rstrip('\n'))
print(max)