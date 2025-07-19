import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name,price", [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988),
        ("", 0),
        ("Булка", -100)
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self):
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_name() == "Краторная булка N-200i"

    def test_get_price(self):
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_price() == 1255
