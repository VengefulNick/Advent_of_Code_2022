# To help prioritize item rearrangement, every item type can be converted to a priority:
#    Lowercase item types a through z have priorities 1 through 26.
#    Uppercase item types A through Z have priorities 27 through 52.
with open('rugsacks.txt', 'r') as file:
    lines = file.read().splitlines()

prio_count = 0

for line in lines:
    half = len(line) // 2
    first = line[half:]
    second = line[:half]

    # Print first and second half on each line to see that they are equal split
    print(first)
    print(second)

    check, = set(first) & set(second)
    # Print the character that occurs in both halves.
    print(check)
    print()

    # Check the prio value of the character occurring in both halves and sum them in prio_count.
    if check >= "a":
        prio_count += ord(check) - ord("a") + 1
    else:
        prio_count += ord(check) - ord("A") + 27

print(prio_count)

# Big thanks to hyper-neutrino at GitHub for getting me past the last part of this task.
