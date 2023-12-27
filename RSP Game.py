import random
def gameWin(you , computer):
    if computer == you:
        return None
    if computer == 'P':
        if you == 'S':
            return True
        elif you == 'R':
            return False
        
    if computer == 'S':
        if you == 'R':
            return True
        elif you == 'P':
            return False
        
    if computer == 'R':
        if you == 'P':
            return True
        elif you == 'S':
            return False
    


computer = ("Computer's choice among Rock (R) , Paper (P) , Scissor (S)")
randNo = random.randint(1,3)
if randNo == 1:
    computer = 'R'
elif randNo == 2:
    computer = 'P'
else:
    computer = 'S'

print(" Welcome to RSP Game ^0^")  
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
round = int(input("Enter number of rounds---->"))
counter = 0
playerWin = 0
compWin = 0
while counter != round:
    you = input("Enter your choice among Rock (R) , Paper (P) , Scissor (S)--->")
    result = gameWin (you, computer)
    print(f"Compter's choice--->{computer}")
    print(f"Your choice--->{you}")
    if result == None:
        print("The game is tied !!!")
    elif result == True:
        print("Congratulations !!! You win this game ")
        playerWin = playerWin +1
    else:
        print("Opps !!! Computer wins this game ")
        compWin = compWin +1
    counter = counter + 1

print("Round finish~~~~~")
if playerWin > compWin:
  print("You are the champion /w(ﾟДﾟ)w/ !!!!!")
else:
    print("Sorry /＞﹏＜/ better luck next time")





