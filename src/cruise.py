from src.ship import Ship


class Cruise(Ship):
    def __init__(self, draft=0.0, crew=0, passengers=0):
        self.passengers = passengers
        Ship.__init__(self, draft, crew)

    def is_worth_it(self):
        if self.draft < 0.0 or self.crew < 0 or self.passengers < 0:
            raise Exception("Error, negative values are not accepted")
        load = self.draft
        load = load - (self.passengers*2.25) - (self.crew*1.5)
        if load > 20:
            return True
        else:
            raise Exception("No fue saqueado")

    def print_crew(self) -> None:
        print(self.crew)

