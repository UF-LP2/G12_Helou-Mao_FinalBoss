
import csv
from cruise import Cruise
from ship import Ship
from cargo import Cargo
def abrir(name):
    barcos = []
    extra = 0
    crew = 0
    quality = 0
    draft = 0
    cont = 0
    with open(name) as file:
        reader = csv.reader(file)
        for row in reader:
            if cont != 0:
                draft = row[0]
                crew = row[1]
                extra = row[2]
                quality = row[3]
                # vamos a tener que verlo mañana
                if quality == 0 and extra == 0:
                    barcos.append(Ship(draft, crew))
            cont = cont + 1

