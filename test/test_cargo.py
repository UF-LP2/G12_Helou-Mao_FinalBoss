from src.cargo import Cargo
import pytest
class TestCargo:

    def test_worth_it_true(self):
        barco = Cargo(200, 8, 30, 1)
        assert barco.is_worth_it() is True

    def test_worth_it_invalid(self):
        with pytest.raises(Exception) as exif:
            barco = Cargo(10, 7, 15, 1)
            assert str(exif.value) == "Error, invalid quantity"
        with pytest.raises(Exception) as exif:
            barco = Cargo(-10, 7, 15, 1)
            assert str(exif.value) == "Error, invalid quantity"

    def test_worth_it_false(self):
        with pytest.raises(Exception) as exif:
            barco = Cargo(10, 7, 15, 2)
            assert str(exif.value) == "Error, invalid values"


