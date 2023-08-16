from src.cruise import Cruise
import pytest
class TestCruise:
    def test_worth_it_negatives(self):
        with pytest.raises(Exception) as exif:
            barco = Cruise(-23, 7, 15)
            assert str(exif.value) == "Error, negative values are not accepted"



    def test_worth_it_false(self):
        with pytest.raises(Exception) as exif:
            barco = Cruise(10, 7, 15)
            assert str(exif.value) == "Error, invalid quantity"
    def test_worth_it_true(self):
        barco = Cruise(120, 10,8)
        assert barco.is_worth_it() is True
