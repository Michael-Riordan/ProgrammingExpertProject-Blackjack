from hand import Hand 

class Dealer:
    def __init__(self):
        self.hand = []

    def get_str_hand(self):
        str_rep = []
        for cards in self.hand:
            for card in cards:
                str_rep.append(card + ",")
                

        x = ' '.join(str_rep)
        return x[:-1]


    def get_value(self):
        points = 0

        for list in self.hand:
            for card in list:
                value = card[0]
                while value != "A":

                    if value in ["K", "J", "Q", "T"]:
                        points += 10
                        break
                
                    elif value.isdigit():
                        points += int(value)
                        break

        for list in self.hand:
            for card in list:
                value = card[0]
                if value == "A":
                    if points + 11 > 21:
                        points += 1

                    if points + 11 <= 21:
                        points += 11
                            

        return points








        

        



