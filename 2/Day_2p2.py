points = 0

with open('input.txt', 'r') as file:
    turns = file.read().splitlines()

print(turns)

# Opponent:
# A = ROCK | B = PAPER | C = SCISSOR

# Mine:
# X = LOSE | Y = DRAW | Z = WIN
# 1p ROCK | 2p PAPER | 3p SCISSOR
# WIN = 6p | DRAW = 3p | LOSS = 0p

for turn in turns:
    # A LOSE | 0 + 3
    if turn == "A X":
        points += 3
    # A DRAW | 3 + 1
    elif turn == "A Y":
        points += 4
    # A WIN | 6 + 2
    elif turn == "A Z":
        points += 8
    # B LOSE | 0 + 1
    elif turn == "B X":
        points += 1
    # B DRAW | 3 + 2
    elif turn == "B Y":
        points += 5
    # B WIN | 6 + 3
    elif turn == "B Z":
        points += 9
    # C LOSE | 0 + 2
    elif turn == "C X":
        points += 2
    # C DRAW | 3 + 3
    elif turn == "C Y":
        points += 6
    # C WIN | 6 + 1
    elif turn == "C Z":
        points += 7
    else:
        "SUM TING WONG!"

print(points)
