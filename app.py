import random,time,os


def mainMenu():
    os.system("cls")
    player1 = input("Player 1 --  ").title()
    player2 = input("Player 2 --  ").title()
    time.sleep(2)
    print("Welcome")
    time.sleep(2)
    startGame(player1,player2)
def startGame(player1,player2):
    os.system("cls")
    input(f"Rank of {player1} \nRoll the Dice --  ")
    move1Number = random.randint(1,6)
    time.sleep(2)
    print("Your Number --  ", move1Number)
    input(f"Rank of {player2} \nRoll the Dice --  ")
    move2Number = random.randint(1,6)
    time.sleep(2)
    print("Your Number --  ", move2Number)

    if move1Number > move2Number:
        print("Winning Player --  ",player1)
    elif move1Number < move2Number:
        print("Winning Player --  ",player2)
    elif move1Number == move2Number:
        print("The Game Is a Draw")
        time.sleep(2)
        startGame(player1,player2)
mainMenu()