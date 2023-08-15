from src.ship import Ship


class Cargo(Ship):
    def __init__(self, cargo=0.0, quality=0.0, draft=0.0, crew=0):
        Ship.__init__(self, draft, crew)
        self.cargo = float(cargo)
        self.quality = float(quality)

    def is_worth_it(self):
        carga = self.draft
        carga = carga-(self.crew*1.5)   # restamos el peso que agrega la tripulacion
        if self.quality == 1:
            carga = carga - 3.5 * self.cargo
        elif self.quality == 0.5:
            carga = carga - 2 * self.cargo
        elif self.quality == 0.25:
            carga = carga - 0.5 * self.cargo
        if carga > 20:
            return True
        else:
            return False


