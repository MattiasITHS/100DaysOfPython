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
import random

my_list = [rock, paper, scissors]

player1 = int(input("Type 1 for rock, 2 for paper, 3 for scizzors "))
if player1 >= 4:
    print("Invalid number. You lose!")
else:
    computer = random.randint(1, 3)

    player_choise = my_list[int(player1) - 1]
    print(my_list[int(player1) - 1])

    computer_choise = my_list[int(computer) - 1]
    print(my_list[int(computer) - 1])

    if player_choise == my_list[0] and computer_choise == my_list[2] or player_choise == my_list[
        1] and computer_choise == my_list[0] or player_choise == my_list[2] and computer_choise == my_list[1]:
        print("You win!")
    elif player_choise == computer_choise:
        print("It's a draw")
    else:
        print("You lose!")