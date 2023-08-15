class Ship:  # draft: peso total , crew: personas
    def __init__(self, draft=0.0, crew=0):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if self.draft < 0.0 or self.crew < 0:
            raise ValueError("Error, negative values are not valid")

        load = self.draft - self.crew*1.5
        if load > 20:
            return True
        else:
            raise ValueError("Error, invalid quantity")

    def print_crew(self) -> None:
        print(self.crew)

