from src.ship import Ship


class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        Ship.__init__(self, draft, crew)
        self.passengers = passengers
    def is_worth_it(self):
        carga = self.draft
        carga = carga - (self.passengers*2.25) - (self.crew*1.5)
        if carga > 20:
            return True
        else:
            return False