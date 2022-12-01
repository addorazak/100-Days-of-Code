import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
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

# Write your code below this line 👇
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Enter a right choice!!!")

# Computer Selection should be random
computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"Computer chose:\n {rock}")
elif computer_choice == 1:
    print(f"Computer chose:\n {paper}")
else:
    print(f"Computer chose:\n {scissors}")

# Rock wins against scissors.
# Paper wins against rock.
# Scissors win against paper.

# Comparing Players choice and the Computers choice
if (player_choice == 0) and (computer_choice == 2):
    print("You won")
elif (computer_choice == 0) and (player_choice == 2):
    print("Ypu lose")
elif (player_choice == 1) and (computer_choice == 0):
    print("You won")
elif (computer_choice == 1) and (player_choice == 0):
    print("You loss")
elif (player_choice == 2) and (computer_choice == 1):
    print("You won")
elif (computer_choice == 2) and (player_choice == 1):
    print("You lose")
elif player_choice == computer_choice:
    print("You tie, Play again!")
