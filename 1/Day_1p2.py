with open('input.txt', 'r') as file:
    calories = file.readlines()

first = 0
second = 0
third = 0
cur_cal = 0

for elf in calories:
    if elf != '\n':
        cur_cal += int(elf)
    else:
        if cur_cal > first:
            second = first
            third = second
            first = cur_cal
            cur_cal = 0
        elif cur_cal > second:
            third = second
            second = cur_cal
            cur_cal = 0
        elif cur_cal > third:
            third = cur_cal
            cur_cal = 0
        else:
            cur_cal = 0
print(first)
print(second)
print(third)

print(first + second + third)
