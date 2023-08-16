from src.lecturaArchivo import read_file


def main() -> None:
    ship = []
    ship = read_file()

    for i in range(len(ship)):
        x = ship[i]
        try:
            booleano = x.is_worth_it()
            print("\n Se saquea")
        except Exception:
            print("\n No se saquea")


if __name__ == "__main__":
    main()
