while True:
    player1 = input("rock-paper-scissors: ")
    player2 = input("rock-paper-scissors: ")
    if player1 == player2:
        print("draw")
    elif player1 == "rock":
        if player2 == "paper":
            print("player2")
        elif player2 == "scissors":
            print("player1")
    elif player1 == "paper":
        if player2 == "rock":
            print("player1")
        elif player2 == "scissors":
            print("player2")
    elif player1 == "scissors":
        if player2 == "rock":
            print("player2")
        elif player2 == "paper":
            print("player1")
    
    nastavi = input("nastavi yes/no")
    if nastavi == "no":
        break
