# Author- Shudhanshu Raj

# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program will ask the user for their input.
# This project will better your understanding of while loops and if statements.

import random
from math import fabs
list1 = [ "Rock", "papper", "Scissor", "rock", "Papper", "scissor" ]

trial = int(input('Enter number of trial: '))
computer=0
user=0

for i in range(trial):
    comp=random.choice(list1)
    u=input('Enter your choice: ')
    if comp =="rock" or comp=="Rock":
        if u=="rock" or u=="Rock":
            print("Match Tie!")
        elif u=="Papper" or u=="papper":
            print("Congatulations! You Won this match.")
            user+=1
        elif u=="Scissor" or u=="scissor":
            print("Ooops! You lost this match.")
            computer+=1
    elif comp =="Papper" or comp=="papper":
        if u=="rock" or u=="Rock":
            print("Ooops! You lost this match.")
            computer+=1
        elif u=="Papper" or u=="papper":
            print("Match Tie!")
        elif u=="Scissor" or u=="scissor":
            print("Congatulations! You Won this match.")
            user+=1
    else:
        if u=="rock" or u=="Rock":
            print("Congatulations! You Won this match.")
            user+=1
        elif u=="Papper" or u=="papper":
            print("Ooops! You lost this match")
            computer+=1
        elif u=="Scissor" or u=="scissor":
            print("Match Tie!")
if computer>user:
       print("You Lost this series by %d - %d"%(computer,trial))
       print("Tie matches= %d"%(fabs(computer-user)))
elif computer<user:
    print("You Won this series by %d - %d"%(user,trial))
    print("Tie matches= %d"%(fabs(computer-user)))
else:
    print("Series Draw")
