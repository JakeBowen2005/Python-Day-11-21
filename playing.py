import os
dealer_cards = [11,1,2,3,4,11]
os.system("clear")

def changeCards(cards):
    for i in range(len(cards)):
        if cards[i] == 11:
            cards[i] = 1

def change2(cards):
    for card in cards: # doesnt change value dont know why
        if card == 2:
            card = 99
    
#changeCards(dealer_cards)
change2(dealer_cards)

print(dealer_cards)