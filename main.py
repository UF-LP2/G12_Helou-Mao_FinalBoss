from src.lecturaArchivo import read_file
from src.ship import Ship
import csv
from src.cargo import Cargo
from src.cruise import Cruise


def main() -> None:
    ship = read_file()
    for x in ship:
        print(x.crew)


if __name__ == "__main__":
    main()
