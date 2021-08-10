p1_call = input("Player 1, Enter rock/paper/scissors: ")
p2_call = input("Player 2, Enter rock/paper/scissors: ")

def rock_paper_scissors(player_1, player_2):
    a_list = ["rock", "paper", "scissors"]

    while player_1 not in a_list or player_2 not in a_list:
        print ("Invalid input. Please give a valid input.")
        player_1 = raw_input("Player 1, Enter rock/paper/scissors: ")
        player_2 = raw_input("Player 2, Enter rock/paper/scissors: ")

    while player_1 == player_2:
        print ("Nobody wins. Try again")
        player_1 = raw_input("Player 1, Enter rock/paper/scissors: ")
        player_2 = raw_input("Player 2, Enter rock/paper/scissors: ")

    if player_1 == "rock" and player_2 == "paper":
        print ("Player 2 wins!")

    elif player_1 == "paper" and player_2 == "rock":
        print ("Player 1 wins!")

    elif player_1 == "rock" and player_2 == "scissors":
        print ("Player 1 wins!")

    elif player_1 == "scissors" and player_2 == "rock":
        print ("Player 2 wins")

    elif player_1 == "paper" and player_2 == "scissors":
        print ("Player 2 wins!")

    elif player_1 == "scissors" and player_2 == "paper":
        print ("Player 1 wins!")

rock_paper_scissors(p1_call,p2_call)