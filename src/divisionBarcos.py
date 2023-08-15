from typing import List

from src.cargo import Cargo
from src.cruise import Cruise
from src.ship import Ship

ship = [Ship]
import csv
def read_file():
   
    with open("ships.csv") as f:
        global ship
        reader = csv.reader(f)
        for x in reader:
            if(x[3]!= ""): #es un cargo
                ship.append(Cargo(x[2], x[3], x[0], x[1]))
            if( x[2]!=""): #ES UN crucero
                ship.append(Cruise(x[2],x[0],x[1]))
            else:
                ship.append(Ship(x[0],x[1]))

    f.close() #no necesario, se cierra solo

   

