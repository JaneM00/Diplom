# test_bun.py
import pytest
from unittest.mock import Mock
from praktikum.bun import Bun

class TestBun:
    def test_bun_initialization(self):
        """
        Проверяет корректность инициализации объекта Bun
        """
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.name == "Краторная булка N-200i"
        assert bun.price == 1255

    def test_get_name(self):
        """
        Проверяет, что метод get_name() возвращает правильное название булки
        """
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        assert bun.get_name() == "Флюоресцентная булка R2-D3"

    def test_get_price(self):
        """
        Проверяет, что метод get_price() возвращает правильную цену булки
        """
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_price() == 1255

    @pytest.mark.parametrize("name,price", [
        ("", 0),
        ("Булка", -100),
        ("Очень длинное название булки больше 50 символов 1234567890", 999),
        ("Special!@#$%^&*()", 100)
    ])
    def test_bun_edge_cases(self, name, price):
        """
        Проверяет крайние случаи при инициализации Bun
        """
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price
