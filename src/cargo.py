from src.ship import Ship


class Cargo(Ship):
    def __init__(self, cargo, quality, draft, crew):
        Ship.__init__(self, draft, crew)
        self.cargo = cargo
        self.quality = quality

    def is_worth_it(self):
        carga = self.draft
        carga = carga-(self.crew*1.5) - self.cargo  # restamos el peso que agrega la tripulacion
        if self.quality == 1:
            carga = carga - 3.5
        elif self.quality == 0.5:
            carga = carga - 2
        elif self.quality == 0.25:
            carga = carga - 0.5
        if carga > 20:
            return True
        else:
            return False


