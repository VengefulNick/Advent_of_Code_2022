# To help prioritize item rearrangement, every item type can be converted to a priority:
#    Lowercase item types a through z have priorities 1 through 26.
#    Uppercase item types A through Z have priorities 27 through 52.
with open('rugsacks.txt', 'r') as file:
    lines = file.read().splitlines()

prio_count = 0
groups = []

for i in range(0, len(lines), 3):
    groups.append([lines[i], lines[i+1], lines[i+2]])

for group in groups:
    first = group[0]
    second = group[1]
    third = group[2]

    check, = set(first) & set(second) & set(third)

    if check >= "a":
        prio_count += ord(check) - ord("a") + 1
    else:
        prio_count += ord(check) - ord("A") + 27

print(prio_count)

# Big thanks to hyper-neutrino at GitHub for getting me past the last part of this task.
