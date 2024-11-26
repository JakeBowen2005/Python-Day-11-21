import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def checkWin(cards):
    if sum(cards) == 21:
        return True
    else:
        return False
    
def checkBust(cards):
    if sum(cards) > 21:
        return True
    else:
        return False
    
def check17(cards):
    if sum(cards) == 17:
        return True
    else:
        return False
    
def checkLess(cards):
    if sum(cards) < 21:
        return True
    else:
        return False
    
def checkBustwithAce(cards):
    if sum(cards) > 21:
        if 11 in cards:
            return True
    else:
        return False
def over17(cards):
    if sum(cards) > 17:
        return True
    else:
        return False
    
# print(player_cards)
# print(dealer_cards)

# def wantAnothaCard(player_cards, cards):
#     hit_pass = str(input("Do you want another card type 'y' or 'no' \n" ))
#     if hit_pass == "y":
#         player_cards.append(random.choice(cards))
#         if (checkWin(player_cards)):
#             print(f"Your cards are {player_cards}")
#             print("Blackjack you win!")
#         if (checkBust(player_cards)):
#             print(f"Your cards are {player_cards}")
#             print("You went over 21, Bust")
#             return
#         else:
#             print(f"Your cards are {player_cards}")




while True:
    os.system("clear")
    player_cards = []
    dealer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

    dealer_cards.append(random.choice(cards))

    print(f"Your cards are {player_cards}: {sum(player_cards)}")
    print(f"Dealers cards: {dealer_cards}") 
    while True:
        if (checkWin(player_cards)):
                print("Blackjack you win!")
                print(f"Your cards are {player_cards}: {sum(player_cards)}")
                exit()
        hit_pass = str(input("Do you want another card type 'y' or 'n' \n" )).lower()
        if hit_pass == "y":
            player_cards.append(random.choice(cards))
            if (checkWin(player_cards)):
                print("Blackjack you win!\n")
                print(f"Your cards are {player_cards}: {sum(player_cards)}\n")
                break
            if (checkBustwithAce(player_cards)):
                for i in range(len(player_cards)):
                    if player_cards[i] == 11:
                        player_cards[i] = 1
                        break
                player_cards.append(random.choice(cards))
                print(f"Your cards are {player_cards}: {sum(player_cards)}\n")
            if (checkBust(player_cards)):
                print("You went over 21, Bust\n")
                print(f"Your cards are {player_cards}: {sum(player_cards)}\n")
                break
            print(f"Your cards are {player_cards}: {sum(player_cards)}\n")
        elif hit_pass == "n":
            break
        else:
            print("Invalid input pleas enter a 'y' or a 'n'")

    while True:
        dealer_cards.append(random.choice(cards))

        if checkWin(dealer_cards):
            print("Dealer got blackjack. You lost!\n")
            print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
            break
        if checkBustwithAce(dealer_cards):
            for i in range(len(dealer_cards)):
                if dealer_cards[i] == 11:
                    dealer_cards[i] = 1
                    break
            dealer_cards.append(random.choice(cards))
        if checkBust(dealer_cards):
            print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
            print("Dealer went over 21. You won\n")
            print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
            break
        if check17(dealer_cards):
            if sum(player_cards) < 17:
                print("You lost sorry\n")
                print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
                break
            elif sum(player_cards) == 17:
                print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
                print("Draw\n")
                break
            else:
                print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
                print("Winner!")
                break
        if over17(dealer_cards):
            if sum(player_cards) > sum(dealer_cards):
                print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
                print("You won!!\n")
                break
            elif sum(player_cards) == sum(dealer_cards):
                print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
                print("Draw\n")
                break
            else:
                print(f"Dealers card {dealer_cards}: {sum(dealer_cards)}")
                print("You lost sorry!\n")
                break

    play_again = input("Do you want to play another game? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        print("Thanks for playing Blackjack! Goodbye!")
        break


    # while True: #fix this game loop to see if the user wants to play again
    #     play_again = str(input(print("Do you want to play again 'y' or 'n'\n")))
    #     if play_again == "n":
    #         print("Thanks for playing see ya later")
    #         BlackJack = False
    #     elif play_again == "y":
    #         os.system("clear")
    #         break
    #     else:
    #         print("Please enter a valid input 'y' or 'n'\n")
    # play_again = str(input(print("Do you want to play again 'y' or 'n'\n")))
    # if play_again == "n":
    #     print("Thanks for playing see ya later")
    #     BlackJack = False
    # elif play_again == "y":
    #     os.system("clear")



    



