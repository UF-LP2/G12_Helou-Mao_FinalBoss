from src.ship import Ship


class Cargo(Ship):
    def __init__(self, draft=0.0, crew=0, cargo=0, quality=0.0):
        self.cargo = cargo
        self.quality = quality
        Ship.__init__(self, draft, crew)

    def is_worth_it(self):

        if self.draft < 0.0 or self.crew < 0 or self.quality < 0 or self.cargo < 0 or self.quality > 1:
            raise Exception("Error, invalid values")
        load = self.draft
        load = load - (self.crew * 1.5)  # subtraction of extra weight
        if self.cargo != 0:
            if self.quality == 1:
                load = load - 3.5 * self.cargo
            elif self.quality == 0.5:
                load = load - 2 * self.cargo
            elif self.quality == 0.25:
                load = load - 0.5 * self.cargo
        if load > 20:
            return True
        else:
            raise Exception("No fue saqueado")

    def print_crew(self) -> None:
        print(self.crew)
