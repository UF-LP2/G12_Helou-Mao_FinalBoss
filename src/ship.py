class Ship:  # draft: peso total , crew: personas
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it (self) :
        carga = self.draft - self.crew*1.5
        if carga > 20:
            return True
        else:
            return False


