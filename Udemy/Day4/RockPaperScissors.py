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

possible_actions = [rock, paper, scissors]
player_action = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_action = random.randint(0, 2)

if player_action < 0 or player_action > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
    exit()

print("Player chose:")
print(possible_actions[player_action])
print("Computer chose:")
print(possible_actions[computer_action])

if player_action == computer_action:
    print("It's a draw.")
elif (player_action == rock and computer_action == scissors) or \
     (player_action == paper and computer_action == rock) or \
     (player_action == scissors and computer_action == paper):
    print("You win!")
else:
    print("You lose.")
