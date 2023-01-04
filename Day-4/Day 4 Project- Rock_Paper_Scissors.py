import random
rocks = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papers = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input = input("What do you choose? Type 0,1,2 for rock,paper,sissors")

op = [rocks,papers,scissors]
computer_input = random.randint(0,len(op)-1)

# Computer input 
print("Computer is: ", computer_input)
comp = computer_input
print(op[computer_input])

# User input
print("User is: ",user_input)
user = int(user_input)
print(op[int(user_input)])

if user == 0 and comp == 0:
    print("Draw!")
elif user == 2 and comp == 2: 
    print("Draw!")
elif user == 1 and comp == 1:
    print("Draw!")
elif user == 0 and comp == 2: 
    print("You win!")
elif user == 1 and comp == 0:
    print("You win!")
elif user == 2 and comp == 1:
    print("You win!")
elif user == 2 and comp == 0: 
    print("You lose!")
elif user == 0 and comp == 1:
    print("You lose!")
elif user == 1 and comp == 2:
    print("You lose!")
else:
    print("error!")


