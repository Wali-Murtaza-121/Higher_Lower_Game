
import random
from art import logo, vs
from game_data import data

def compare(random_choice1, random_choice2):
  if random_choice1['follower_count'] > random_choice2['follower_count']:
    return random_choice1['name']
  elif random_choice1['follower_count'] < random_choice2['follower_count']:
    return random_choice2['name']
  else:
    return "Draw"

def score_decider(random_choice1,random_choice2,final_result,user_choice):
  if (user_choice == "a" and final_result == random_choice1['name']) or (user_choice == "b" and final_result == random_choice2['name']):
    return 1
  else:
    return 0

def game():
  random_choice1 = random.choice(data)
  random_choice2 = random.choice(data)
  score = 0
  should_continue = True
  while should_continue:
    print(logo)
    print(
    f"Compare A: {random_choice1['name']}, a {random_choice1['description']}, from {random_choice1['country']}."
  )

    print(vs)

    print(
    f"Against B: {random_choice2['name']}, a {random_choice2['description']}, from {random_choice2['country']}."
  )
    final_result = compare(random_choice1, random_choice2)
    user_choice  = input("Who has more followers? Type 'A' or 'B': ").lower()
    score += score_decider(random_choice1,random_choice2,final_result,user_choice)
    
    print(f"Current Score is: {score}.")
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again != "y":
        should_continue = False
        print(f"Final score is: {score}.")
    else:
        should_continue = True
        random_choice1 = random.choice(data)
        random_choice2 = random.choice(data)

game()