import csv
from src.cargo import Cargo
from src.cruise import Cruise
from src.ship import Ship


def is_int(aux):
    if aux == "":
        numero = 0
        return numero
    else:
        numero = int(aux)
        if type(numero) == int:
            return numero
        else:
            raise Exception


def is_float(aux):
    if aux == "":
        numero = 0.0
        return numero
    else:
        numero = float(aux)
        if type(numero) == float:
            return numero
        else:
            raise Exception



def read_file() :
    ship = [Ship]
    with open("ships.csv") as f:

        reader = csv.reader(f)
        next(f)
        for x in reader:

            if x[3] != "":
                try:
                    aux1 = is_int(x[1])
                    aux = is_float(x[0])
                    aux2 = is_int(x[2])
                    aux3 = is_float(x[3])
                except:
                    print("Invalid value cargo")
                if x[2]=="":
                    shipaux = Cargo(aux, aux1, 0, aux3)
                else:
                    shipaux = Cargo(aux, aux1, aux2, aux3)
                ship.append(shipaux)

            elif x[2] != "":  # es un cruise
                try:
                    aux1 = is_int(x[1])
                    aux = is_float(x[0])
                    aux2 = is_int(x[2])
                except:
                    print("Invalid value cruise")

                shipaux = Cruise(aux, aux1, aux2)
                ship.append(shipaux)
            else:
                try:
                    aux1 = is_int(x[1])
                    aux = is_float(x[0])
                except:
                    print("Invalid value ship")
                shipaux = Ship(aux, aux1)
                ship.append(shipaux)


    f.close()  # not necessary
    return ship
