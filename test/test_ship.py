import pytest
from src.ship import Ship


class TestShip:

    def test_worth_it_negatives(self):
        with pytest.raises(Exception) as exif:
            barco = Ship(-23, 7)
            assert str(exif.value) == "Error, invalid values"

    def test_worth_it_true(self):
        barco = Ship(30, 5)
        assert barco.is_worth_it() is True

    def test_worth_it_false(self):
        with pytest.raises(Exception) as exif:
            barco = Ship(-23, 7)
            assert str(exif.value) == "No fue saqueado"


