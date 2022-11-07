from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def reset(self):
        self.player.hand = []
        self.dealer.hand = []
        self.bet = None
        self.deck = Deck()

    def confirm_start(self):
        start_prompt = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ").lower()
        
        return start_prompt in ["y", "yes", "start"]
    
    def place_bet(self):
        
        while True:
            
            try:
                bet = float(input("Place your bet: "))

                if float(bet) < Game.MINIMUM_BET:
                    print(f"The minimum bet is {Game.MINIMUM_BET}.")
                

                elif float(bet) > self.player.balance:
                    print(f"You do not have sufficient funds.")
                
                else:

                    self.bet = float(bet)
                    self.player.balance -= float(bet)
                    break

            except ValueError as e:
                print("Not a valid input.")

    def derive_winner(self):

        if self.dealer.get_value() > self.player.get_value():
            print(f"The dealer wins. You lose ${self.bet}")
            self.reset()
            return True
            
            

        elif self.player.get_value() > self.dealer.get_value():
            print(f"You have the higher hand and win ${self.bet}")
            self.player.balance += (self.bet * 2)
            self.reset()
            return True
            

        else:
            print("You tie. Your bet has been returned")
            self.player.balance += self.bet
            self.reset()
            return True
            
    def hit(self):

        new_dealt = self.deck.deal(1, 1)
        self.player.hand.append(new_dealt[0])

        print(f"You now have: {self.player.get_str_hand()}")
        
        if self.player.get_value() > 21:
            print(f"Your hand value is over 21 and you lose {self.bet} :(")
            self.reset()
            return False
        
        else:
            return True

    def stay(self):
        while True:

            
                
            if self.dealer.get_value() == 21:
                print(f"The dealer has a natural!! You lose ${self.bet}")
                self.reset()
                break
                        
                        
                
            while self.dealer.get_value() <= 16:
                next_card = self.deck.deal(1, "hit")[1][0]
                ' '.join(next_card)
                self.dealer.hand.append(next_card)
                print(f"The dealer has: {self.dealer.get_str_hand()}")
                        
                        
            if self.dealer.get_value() > 21:
                print(f"The dealer busts. You win {self.bet}")
                self.player.balance += (self.bet * 2)
                self.reset()
                break
                        

            else:
                print("The dealer stays.")
                if self.derive_winner() == True:
                    break

    def round_one(self):

        while True:

            hit_or_stay = input("Would you like to hit or stay? ").lower()
            if hit_or_stay not in ["hit", "stay"]:
                print("That is not a valid option.")

            elif hit_or_stay == "hit":
                if self.hit() == False:
                    break

                else:
                    continue
                


            elif hit_or_stay == "stay":
                print(f"The dealer has: {self.dealer.get_str_hand()}")
                self.stay()
                break
   
    def handle_blackjack(self):
        blackjack = self.player.get_value() == 21

        if blackjack:
            print(f"The dealer has: {self.dealer.get_str_hand()}")
            if self.dealer.get_value() == 21:
                print("You tie, your bet has been returned.")
                self.player.balance + self.bet
                return True
            else:
                print(f"BlackJack! You win ${self.bet * 1.5} :)")
                self.player.balance += self.bet
                self.player.balance += (self.bet * 1.5)
                self.reset()
                return True

    def check_balance(self):
        if self.player.balance == 0:
            print("You've run out of money, please restart the program to play again.")           

    def start_game(self):

        
        
        while self.player.balance > 0:
            print()
            
            if not self.confirm_start():
                print(f"You leave with ${self.player.balance}. Goodbye.")
                break

            else:
                self.place_bet()
                dealt_cards = self.deck.deal(2, "start")
                player_cards = dealt_cards[0]
                self.player.hand.append(player_cards)
                dealer_cards = dealt_cards[1]
                self.dealer.hand.append(dealer_cards)
                
            while not self.handle_blackjack():
                self.round_one()
                break

        self.check_balance()

    
                
            

        
        



            