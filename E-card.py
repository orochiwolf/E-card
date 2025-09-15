SHORT_TO_FULL = {
    "E": "Emperor",
    "C": "Citizen",
    "S": "Slave"
}
# Card constants
EMPEROR = "E"
CITIZEN = "C"
SLAVE = "S"
#game parameter
max_round = 12 #max round play
round_swap = 3 #decide when the swap of hand happend
round = 1 #follow the actual round
score_player1 = 0
score_player2 = 0

#EMPEROR Hand
hand1 = [EMPEROR] + [CITIZEN] * 4
#Slave Hand
hand2 = [SLAVE] + [CITIZEN] * 4

tempHand1 = hand1.copy()  #Physical player 1 hand
tempHand2 = hand2.copy()  #Pysical player 2 hand
#game loop
while (round <= max_round):
    print(f"You are playing the round: {round}")
    print(f"The actual score is : Player1: {score_player1} && Player2: {score_player2}")

    #player 1 choose
    choice1 = input("choose from your hand (E/C)")
    isCardExist = False
    while(isCardExist == False):
        if choice1.upper() in tempHand1:
            isCardExist = True
            tempHand1.remove(choice1)
            print(f"Player 1 choose his card")
        else:
            print("❌ Invalid choice! That card is not in your hand, try again.")
            choice1 = input("choose from your hand (E/C)")

    #player 2 choose
    choice2 = input("choose from your hand (S/C)")
    isCardExist = False
    while(isCardExist == False):
        if choice2.upper() in tempHand2:
            isCardExist = True
            tempHand2.remove(choice2)
            print(f"Player 2 had choose his card")
        else:
            print("❌ Invalid choice! That card is not in your hand, try again.")
            choice2 = input("choose from your hand (S/C)")
    #reveal result:
    print(f"Player1 has choose : {SHORT_TO_FULL[choice1]}")
    print(f"Player2 has choose : {SHORT_TO_FULL[choice2]}")
    if choice1 == choice2:
        print("Draw!")
    if choice1 == "E" and choice2 == "C":
        score_player1 = score_player1 + 1
        print("Player 1 wins!")
        round += 1
        tempHand1 = hand1.copy()
        tempHand2 = hand2.copy()
    if choice1 == "C" and choice2 == "S":
        score_player1 = score_player1 + 1
        print("Player 1 wins!")
        round += 1
        tempHand1 = hand1.copy()
        tempHand2 = hand2.copy()
    if choice1 == "S" and choice2 == "E":
        score_player1 = score_player1 + 1
        print("Player 1 wins!")
        round += 1
        tempHand1 = hand1.copy()
        tempHand2 = hand2.copy()
    if choice1 == "E" and choice2 == "S":
        score_player2 = score_player2 + 5
        print("Player 2 wins!")
        round += 1
        tempHand1 = hand1.copy()
        tempHand2 = hand2.copy() 
    if choice1 == "C" and choice2 == "E":
        score_player2 = score_player2 + 5
        print("Player 2 wins!")
        round += 1
        tempHand1 = hand1.copy()
        tempHand2 = hand2.copy()
    if choice1 == "S" and choice2 == "C":
        score_player2 = score_player2 + 5
        print("Player 2 wins!")
        round += 1
        tempHand1 = hand1.copy()
        tempHand2 = hand2.copy() 
    print(f"Player 1 hand: {tempHand1}")
    print(f"Player 2 hand: {tempHand2}")
    print(f"Emporor hand: {hand1}")
    print(f"Slave hand: {hand2}")

print(f"{round - 1} rounds were played")
print(f"The final score is : Player1: {score_player1} && Player2: {score_player2}")



