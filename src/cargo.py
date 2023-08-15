from src.ship import Ship


class Cargo(Ship):
    def __init__(self, draft=0.0, crew=0, cargo=0, quality=0.0):
        Ship.__init__(self, draft, crew)
        self.cargo = cargo
        self.quality = quality

    def is_worth_it(self):
        load = self.draft
        load = load - (self.crew * 1.5)  # subtraction of extra weight
        if self.quality == 1:
            load = load - 3.5 * self.cargo
        elif self.quality == 0.5:
            load = load - 2 * self.cargo
        elif self.quality == 0.25:
            load = load - 0.5 * self.cargo
        if load > 20:
            return True
        else:
            raise ValueError("Error, invalid quantity")
