from src.ship import Ship


class Cruise(Ship):
    def __init__(self, draft=0.0, crew=0, passengers=0):
        Ship.__init__(self, draft, crew)
        self.passengers = passengers

    def is_worth_it(self):
        load = self.draft
        load = load - (self.passengers*2.25) - (self.crew*1.5)
        if load > 20:
            return True
        else:
            raise ValueError("Error, invalid quantity")
