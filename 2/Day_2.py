points = 0

with open('input.txt', 'r') as file:
    turns = file.read().splitlines()

print(turns)

# Opponent:
# A = ROCK | B = PAPER | C = SCISSOR
# Mine:
# X = ROCK | Y = PAPER | Z = SCISSOR
#   1p          2p             3p
# WIN = 6p      DRAW = 3p       LOSS = 0p

for turn in turns:
    # A draws X | 3 + 1
    if turn == "A X":
        points += 4
    # A losses to Y | 6 + 2
    elif turn == "A Y":
        points += 8
    # A beats Z | 0 + 3
    elif turn == "A Z":
        points += 3
    # B beats X | 0 + 1
    elif turn == "B X":
        points += 1
    # B draws Y | 3 + 2
    elif turn == "B Y":
        points += 5
    # B losses to Z | 6 + 3
    elif turn == "B Z":
        points += 9
    # C losses to X | 6 + 1
    elif turn == "C X":
        points += 7
    # C beats Y | 0 + 2
    elif turn == "C Y":
        points += 2
    # C draws Z | 3 + 3
    elif turn == "C Z":
        points += 6
    else:
        "SUM TING WONG!"

print(points)
