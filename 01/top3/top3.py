file = open('input.txt', 'r')
lines = file.readlines()
elves = []
current = 0
for l in lines:
    if len(l) == 1:
        elves.append(current)
        current = 0
    else:
        current += int(l.rstrip('\n'))
top3cal = []
total_cal = 0
for i in range(3):
    max = 0
    for elve in elves:
        if elve > max and elve not in top3cal:
            max = elve
    top3cal.append(max)
    total_cal += max

print(top3cal)
print(total_cal)

