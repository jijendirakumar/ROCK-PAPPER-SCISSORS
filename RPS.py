import random

rock =('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper=('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissors=('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game_images =[rock,paper,scissors]

while True :

    user_choise = int(input("what do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choise >= 0 or user_choise <= 2:
        print (game_images[user_choise])

    computer_choise = random.randint(0, 2 )
    print("computer choose :")

    print(game_images[computer_choise])

    if user_choise >= 3 or user_choise <= 0:
        print ("invalid  number")

    elif user_choise == 0 and computer_choise == 2 :
        print("you win!...")

    elif user_choise == 2 and computer_choise == 0 :
        print("computer win ")

    elif computer_choise > user_choise :
        print("computer win!...")

    elif user_choise > computer_choise :
        print("you win!...")

    elif computer_choise < user_choise :
        print("draw")

    else :
        print("computer win!..")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break

