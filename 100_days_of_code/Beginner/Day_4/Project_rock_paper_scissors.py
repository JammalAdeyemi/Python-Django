# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved
#  to a corresponding variable: rock, paper, and scissors. This will make it easy to 
# print them out to the console.

# Start the game by asking the player:
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
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
game = [rock, paper, scissors]
gamer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if gamer >= 3 or gamer < 0: 
  print("You typed an invalid number, you lose!") 
else:

    print(game[gamer])

    computer = random.randint(0,2)
    print(f"Computer choice is {computer}")
    print(game[computer])


    if gamer == 0 and computer == 2:
        print("You win!")
    elif gamer == 2 and computer == 0:
        print("You lose")
    elif computer > gamer:
        print("You lose")
    elif gamer > computer:
        print("You win!")
    elif computer == gamer:
        print("It's a draw")

