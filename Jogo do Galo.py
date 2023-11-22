import sys
import numpy as np

gameboard = np.array([["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"]])
count = 0

def replacegameboard(gameboarde, coordinate, playe):
    for i in range(len(gameboarde)):
        for j in range(len(gameboarde[i])):
            if gameboarde[i][j] == coordinate:
                gameboarde[i][j] = playe
                return gameboarde

def win(gameboardw):
    if gameboardw[0][0] == gameboardw[0][1] and gameboardw[0][1] == gameboardw[0][2]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[1][0] == gameboardw[1][1] and gameboardw[1][1] == gameboardw[1][2]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[2][0] == gameboardw[2][1] and gameboardw[2][1] == gameboardw[2][2]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[0][0] == gameboardw[1][1] and gameboardw[1][1] == gameboardw[2][2]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[0][2] == gameboardw[1][1] and gameboardw[1][1] == gameboardw[2][0]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[0][0] == gameboardw[1][0] and gameboardw[1][0] == gameboardw[2][0]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[0][1] == gameboardw[1][1] and gameboardw[1][1] == gameboardw[2][1]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()
    elif gameboardw[0][2] == gameboardw[1][2] and gameboardw[1][2] == gameboardw[2][2]:
        print(gameboardw)
        print("WIN!!")
        sys.exit()

while True:
    print(np.array(gameboard))
    count += 1
    if count % 2 != 0:
        play = input(f"Input your play Player X:(ex:A1):")
        while play not in gameboard[0] and play not in gameboard[1] and play not in gameboard[2]:
            play = input(f"Input your play Player X:(ex:A1):")
        replacegameboard(gameboard,play, "X")
    else:
        play = input(f"Input your play Player O:(ex:A1):")
        while play not in gameboard[0] and play not in gameboard[1] and play not in gameboard[2]:
            play = input(f"Input your play Player O:(ex:A1):")
        replacegameboard(gameboard, play, "O")
    win(gameboard)
    if count > 8:
        print(gameboard)
        print("DRAW!!")
        gameboard = np.array([["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]])
        count = 0
        restart = input("Start over?:Yes or No?")
        if restart.lower() == "yes":
            print("Restarting the game:")
            gameboard = np.array([["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]])
            count = 0
        elif restart.lower() == "no":
            print("Restartiong the game.")
            sys.exit()