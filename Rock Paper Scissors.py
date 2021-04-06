import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
while True:
    computer_random_choice = random.randint(1, 3)
    if computer_random_choice == 1:
        cpu_choice = 1
        cpu_roll = "Rock"
    if computer_random_choice == 2:
        cpu_choice = 2
        cpu_roll = "Paper"
    if computer_random_choice == 3:
        cpu_choice = 3
        cpu_roll = "Scissors"

    print("\t   Welcome to Rock Paper Scissors . Enter 'quit' to escape.\n\t\tPlease choose 1) Rock 2) Paper 3) Scissors")
    while True:
        player_input = input("Choice: ")
        if player_input.lower() == 'quit':
            print("Thanks for playing")
            quit()
        if player_input.lower() == '1' or player_input == 'rock':
            player_roll = 'Rock'
            player_choice = 1
            # print('player chose Rock')
            break
        if player_input.lower() == '2' or player_input == 'paper':
            player_roll = 'Paper'
            player_choice = 2
            # print('player chose Paper')
            break
        if player_input.lower() == '3' or player_input == 'Scissors':
            player_roll = 'Scissors'
            player_choice = 3
            # print('player choose Scissors')
            break
        if player_input.lower() == 'win':
            print('Player Wins!')
            quit()
        else:
            print("Entry invaild")
            continue

    #Handling Tie results
    if player_choice == 1 and cpu_choice == 1:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nThis was a tie!")
    if player_choice == 2 and cpu_choice == 2:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nThis was a tie!")
    if player_choice == 3 and cpu_choice == 3:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nThis was a tie!")

    #Hanlding player victories
    if player_choice == 1 and cpu_choice == 3:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nPlayer wins!")
    if player_choice == 2 and cpu_choice == 1:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nPlayer wins!")
    if player_choice == 3 and cpu_choice == 2:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nPlayer wins!")

    #Hanlding player losses
    if player_choice == 3 and cpu_choice == 1:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nComputer wins!")
    if player_choice == 1 and cpu_choice == 2:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nComputer wins!")
    if player_choice == 2 and cpu_choice == 3:
        print("The Player picked:", player_roll, "\nThe CPU picked:   ", cpu_roll, "\nComputer wins!")

    input('Press Enter to play again')
    cls()