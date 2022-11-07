import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        for key in Card.VALUE_NAMES:
            name = Card.VALUE_NAMES[key]
            for k in Card.SUIT_SYMBOLS:
                suit = Card.SUIT_SYMBOLS[k]
                new_card = name + suit
                self.cards.append(new_card)
                
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards, round):
        player_dealt_cards = []
        dealer_dealt_cards = []

        while len(self.cards) > 0:


            if round == "start":

                for i in range(num_cards):
                    player_dealt = self.cards.pop()
                    dealer_dealt = self.cards.pop()
                    player_dealt_cards.append(str(player_dealt))
                    dealer_dealt_cards.append(str(dealer_dealt))

                print(f"You are dealt: {player_dealt_cards[0]}, {player_dealt_cards[1]}")
                print(f"The dealer is dealt: {dealer_dealt_cards[0]}, Unknown")
            

            if round == 1:
                new_dealt = []
                player_dealt_next = self.cards.pop()
                new_dealt.append(player_dealt_next)
                player_dealt_cards.append(player_dealt_next)
                print(f"You are dealt {new_dealt[0]}")
            
            if round == "hit":
                card_to_add = []
                next_card = self.cards.pop()
                card_to_add.append(next_card)
                print(f"The dealer hits and is dealt: {next_card}")
                dealer_dealt_cards.append(card_to_add)
            

            return [player_dealt_cards, dealer_dealt_cards]

        else:
            print("There are no more cards in the deck. Please restart the program to play again.")




        

            



        


    