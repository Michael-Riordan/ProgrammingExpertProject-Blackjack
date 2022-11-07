class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.hand = []
        self.add_to_hand()
        

    def get_value(self):
        pass
        
    def add_to_hand(self, cards):
        
        for card in cards:
            self.hand.append(str(card))
        

    def __str__(self):
        pass
