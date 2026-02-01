import random

# Daniel Lewis

faces = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]

suits = ["C","D","H","S"]

player_face = faces[random.randint(0,12)]
player_suit = suits[random.randint(0,3)]
player_draw = player_face + player_suit
player_face_num = int(player_face)
print("Your draw is", player_draw)

bet = int(input("How much do you bet? :"))
bet = round(bet * 3, 2)

computer_face = faces[random.randint(0,12)]
computer_suit = suits[random.randint(0,3)]
computer_draw = computer_face + computer_suit
computer_face_num = int(computer_face)
print("The computer's draw is", computer_draw)

def get_suit_num(suit):
    if suit == "C":
        return 4
    elif suit == "H":
        return 3
    elif suit == "D":
        return 2
    elif suit == "C":
        return 1
    
def win():
    print("You win!")
    print(f"You won €{bet}")

if player_face_num > computer_face_num:
    win()
elif computer_face_num > player_face_num:
    print("You lose!")
else:
    #print("Draw")
    player_suit_num = get_suit_num(player_suit)
    computer_suit_num = get_suit_num(computer_suit)
    if player_suit_num > computer_suit_num:
        win()
    elif computer_suit_num > player_suit_num:
        print("You lose!")
    else:
        print("Draw")
