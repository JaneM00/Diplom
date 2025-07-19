# test_burger.py

import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE

class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def bun(self):
        return Mock()

    @pytest.fixture
    def ingredient(self):
        return Mock()

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == initial_count + 1

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_count - 1

    def test_move_ingredient(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

@patch('praktikum.burger.Bun')
    @patch('praktikum.burger.Ingredient')
    def test_get_price(self, mock_ingredient, mock_bun, burger):
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 50
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == 200  # 100*2 (buns) + 50*2 (ingredients)

    @patch('praktikum.burger.Bun')
    def test_get_receipt(self, mock_bun, burger):
        mock_bun.get_name.return_value = "Краторная булка"
        
        with patch('praktikum.burger.Ingredient') as mock_ingredient:
            mock_ingredient.get_type.return_value = INGREDIENT_TYPE.SAUCE
            mock_ingredient.get_name.return_value = "Соус Spicy-X"
            
            burger.set_buns(mock_bun)
            burger.add_ingredient(mock_ingredient)
            
            receipt = burger.get_receipt()
            
            assert "Краторная булка" in receipt
            assert "Соус Spicy-X" in receipt
            assert "Price: " in receipt
