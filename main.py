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
import random
#Write your code below this line 👇
move = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
move_player = int(move)
move_pc = random.randint(0, 2)
rps = ["rock", "paper", "scissors"]
"""
    Rock wins against scissors.

    Scissors win against paper.

    Paper wins against rock.
"""
#move_player_st = rps[move_player]
#print(move_player_st)
#print(rps[move_pc])
if move_player == 0:
  print(rock)
  if move_pc == 0:
    print(rock)
    print("Draw")
  elif move_pc == 1:
    print(paper)
    print("You lose")
  elif move_pc == 2:
    print(scissors)
    print("You win!!!")
elif move_player == 1:
  print(paper)
  if move_pc == 1:
    print(paper)
    print("Draw")
  elif move_pc == 2:
    print(scissors)
    print("You lose")
  elif move_pc == 0:
    print(rock)
    print("You win!!!")
elif move_pc == 2:
  print(scissors)
  if move_pc == 2:
    print(scissors)
    print("Draw")
  elif move_pc == 0:
    print(rock)
    print("You lose")
  elif move_pc == 1:
    print(paper)
    print("You win!!!")
  else:
    print("You choose wrong")
  
#print(f"your choice {move}, computer choice {move_pc}")