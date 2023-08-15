import pytest
from src.ship import Ship


class TestShip:
    def test_worth_it_false(self):
        barco = Ship(15, 10)
        assert barco.is_worth_it() is False

    def test_worth_it_negatives(self):
        with pytest.raises(ValueError) as exif:
            barco = Ship(-23, 7)
        assert str(exif.value) == "Error, no se aceptan valores negativos"

    def test_worth_it_true(self):
        barco = Ship(30, 5)
        assert barco.is_worth_it() is True


