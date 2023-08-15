from src.lecturaArchivo import read_file
from src.divisionBarcos import *
from src.ship import Ship


def main() -> None:
    ship = [str]
    ships = [Ship]
    ship = read_file()
    cruises = [Cruise]
    cargo_ships = [Cargo]
    cargo_ships = division_cargo_ships(ship)
    ship = delete_ships(cargo_ships, ship)
    cruises = division_cruises(ships)
    ship = delete_ships(cruises, ship)

    for x in ship:
        ships.append(Ship(x))
    print(ships)


if __name__ == "__main__":
    main()
