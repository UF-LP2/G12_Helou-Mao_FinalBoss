class Ship(object):  # draft: peso total , crew: personas
    nships = 0

    def __init__(self, draft=0.0, crew=0):
        self.draft = draft
        self.crew = crew
        Ship.nships = Ship.nships + 1

    def is_worth_it(self):
        if self.draft < 0.0 or self.crew < 0:
            raise Exception("Error, negative values are not accepted")
        load = 0
        load = self.draft - self.crew * 1.5
        if load > 20:
            return True
        else:
            raise Exception

    def print_crew(self) -> None:
        print(self.crew)
