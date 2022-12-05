with open('input.txt', 'r') as file:
    calories = file.readlines()

max_cal = 0
cur_cal = 0

for elf in calories:
    if elf != '\n':
        cur_cal += int(elf)
    else:
        if cur_cal > max_cal:
            max_cal = cur_cal
        cur_cal = 0

print(max_cal)
