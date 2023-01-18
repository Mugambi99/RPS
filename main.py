import random
play = ["Rock", "Paper", "Scissors"]

computer_choice = play[random.randint(0,2)]
print(computer_choice)

player=False

while player==False:
    points=0
    player=input("Select your choice:")
    if player == computer_choice:
        print("Tie")
    elif player=="Rock":
        if computer_choice=="Paper":
            comp_points=points+1
            print(computer_choice, "beats", player, "-YOU LOSE-Computer has", comp_points)
        else:
            player_points=points+1
            print(player, "beats", computer_choice, "-YOU WIN-Player has", player_points)
    elif player=="Paper":
        if computer_choice=="Scissors":
            comp_points1=points+1
            print(computer_choice, "beats", player, "-YOU LOSE-Computer has", comp_points1 )
        else:
            player_points1=points+1
            (player, "beats", computer_choice, "-YOU WIN-Player has", player_points1)
    elif player == "Scissors":
        if computer_choice == "Rock":
            comp_points2=points+1
            print(computer_choice, "beats", player, "-YOU LOSE-Computer has",comp_points2)
        else:
            player_points2=points+1
            print(player, "beats", computer_choice, "-YOU WIN-Player has",player_points2)
    else:
        print("Check spelling/type a vaild choice")
       
    #Player was set to True, but we want it to be False so the loop continues 
    player = False