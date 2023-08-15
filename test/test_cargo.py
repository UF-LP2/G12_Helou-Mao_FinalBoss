from src.cargo import Cargo
class TestCargo:
    def test_worth_it_false(self):
        barco = Cargo(15, 0.5, 15, 10)
        assert barco.is_worth_it() is False

    def test_worth_it_true(self):
        barco = Cargo(30, 1, 200, 8)
        assert barco.is_worth_it() is True
