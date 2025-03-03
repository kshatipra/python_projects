#Rock paper scisscors game
import sys
import random
playerchoice = int(input("Enter ....1, 2 or 3 \n1. Rock \n2. Papers \n3. Scissors"))

if playerchoice < 1 | playerchoice > 3:
    sys.exit("You must enter 1, 2 or 3.")

computer_choice = random.choice("123") #randomly chooses one of the characters from the string. 
computer = int(computer_choice)

print("")
print(f"You choose {playerchoice}.\nComputer chose {computer_choice}.\n")

if playerchoice == computer:
    print("Thats a tie! Enter your choice again!")
elif playerchoice == 1 and computer == 3:
    print("You win!")
elif playerchoice ==2 and computer == 1:
    print("You win!")
elif playerchoice == 3 and computer == 2:
    print("You win!")
else:
    print("Computer Wins!")
