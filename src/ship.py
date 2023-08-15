class Ship:  # draft: peso total , crew: personas
    def __init__(self, draft=0.0, crew=0):
        self.draft = float(draft)
        self.crew = int(crew)

    def is_worth_it(self):
        if self.draft < 0.0 or self.crew < 0:
            raise ValueError("Error, no se aceptan valores negativos")

        cargo = self.draft - self.crew*1.5
        if cargo > 20:
            return True
        else:
            return False


