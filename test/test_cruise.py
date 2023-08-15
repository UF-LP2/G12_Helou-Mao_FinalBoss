from src.cruise import Cruise

class TestCruise:
    def test_worth_it_false(self):
        barco = Cruise(15, 10, 15)
        assert barco.is_worth_it() is False

    def test_worth_it_true(self):
        barco = Cruise(30, 120,8)
        assert barco.is_worth_it() is True
