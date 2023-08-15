import csv
from src.cargo import Cargo
from src.cruise import Cruise
from src.ship import Ship


def is_int(aux):
    if type(aux) == int or aux == "":
        return aux
    else:
        raise Exception


def is_float(aux):
    if type(aux) == float or aux == "":
        return aux
    else:
        raise Exception


def read_file() -> list[Ship]:
    ship = [Ship]
    with open("ships.csv") as f:
        reader = csv.reader(f)
        for x in reader:
            if x[3] != "":
                try:
                    aux1 = is_int(x[1])
                    aux = is_float(x[0])
                    aux2 = is_int(x[2])
                    aux3 = is_float(x[3])
                    shipaux = Cargo(float(x[0]), int(x[1]), int(x[2]), float(x[3]))
                    ship.append(shipaux)
                except:
                    print("Invalid value")

            if x[2] != "":  # es un cruise
                try:
                    aux1 = is_int(x[1])
                    aux = is_float(x[0])
                    aux2 = is_int(x[2])
                    shipaux = Cargo(float(x[0]), int(x[1]), int(x[2]))
                    ship.append(shipaux)
                except:
                    print("Invalid value")
            else:
                try:
                    aux1 = is_int(x[1])
                    aux = is_float(x[0])
                    shipaux = Cargo(float(x[0]), int(x[1]))
                    ship.append(shipaux)
                except:
                    print("Invalid value")

    f.close()  # not necessary
    return ship
