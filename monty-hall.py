import random

WinCount = 0

def GameGenerator():
    doors = ["goat", "goat", "car"]

    random.shuffle(doors)

    return doors

def PickLogic(game):
    PlayerChoice = random.randint(0, len(game) - 1)

    game.pop(PlayerChoice)

    MontyChoice = random.randint(0, len(game) - 1)

    if game[MontyChoice] == "goat":
        game.pop(MontyChoice)
    elif MontyChoice == 0:
        game.pop(MontyChoice + 1)
    else:
        game.pop(MontyChoice - 1)

    global WinCount

    if game[0] == "car":
        WinCount += 1
        print("you win!")
    else:
        print("you lose!")

rounds = 5000

for x in range(rounds):
    PickLogic(GameGenerator())

print(WinCount / rounds * 100)
