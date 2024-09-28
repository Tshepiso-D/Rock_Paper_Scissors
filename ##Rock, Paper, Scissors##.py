##Rock, Paper, Scissors##
import random
#Generate the user's option by letting them type it into the computer.
#Ask the user to select an option Rock, Paper, Scissors#

options=["rock", "paper", "scissors"]

user_score=0

computer_score=0
rounds=0
while True:
    user_pick=input("Type your pick between Rock, Paper or Scissors or select Q to quit. ").lower()
    
    if user_pick == "q":
        break

    if user_pick not in options: 
        continue
    
    print("user_pick is: "+user_pick)
    rounds+=1
#Computer's Pick#
#Use the list option to allow the computer to generate an option using the random module#
    computer_pick_number=random.randint(0,2)
    computer_pick=options[computer_pick_number]
    print("computer pick is: "+computer_pick)
 

#Create the conditions for success and comment on whether the computer or the user has won#
    if user_pick=="rock" and computer_pick=="scissors":
        user_score+=1
        print("You won")

    elif user_pick=="scissors" and computer_pick=="paper":
        user_score+=1
        print("You won")

    elif user_pick=="paper" and computer_pick=="rock":
        user_score+=1
        print("You won")

    elif user_pick==computer_pick:
        user_score+=1
        computer_score+=1
        print ("It's a draw")

    else: 
        print("You lost")
        computer_score+=1

#Add the scores of the different players and give a final result#
print("Computer Score: "+str(computer_score))
print("Your Score: "+str(user_score))
print("You got "+str(user_score)+ " out of "+str(rounds)+" rounds")