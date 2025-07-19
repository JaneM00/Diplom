#burger.py 
import pytest
from unittest.mock import Mock, patch
from burger import Burger, Ingredient


class TestBurger:
    @pytest.fixture
    def sample_ingredients(self):
        return [
            Ingredient("flour", "sauce", 100),
            Ingredient("beef", "main", 200),
            Ingredient("tomato", "filling", 50)
        ]

    @pytest.mark.parametrize("ingredient_type,expected_price", [
        ("sauce", 100),
        ("main", 200),
        ("filling", 50),
        ("unknown", 0)
    ])
    def test_get_price_by_type(self, sample_ingredients, ingredient_type, expected_price):
        burger = Burger()
        for ingredient in sample_ingredients:
            burger.add_ingredient(ingredient)
        
        assert burger.get_price_by_type(ingredient_type) == expected_price

    def test_add_ingredient(self, sample_ingredients):
        burger = Burger()
        initial_count = len(burger.ingredients)
        
        for ingredient in sample_ingredients:
            burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == initial_count + len(sample_ingredients)

    def test_remove_ingredient(self, sample_ingredients):
        burger = Burger()
        for ingredient in sample_ingredients:
            burger.add_ingredient(ingredient)
        
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(sample_ingredients[0])
        
        assert len(burger.ingredients) == initial_count - 1

    def test_get_total_price(self, sample_ingredients):
        burger = Burger()
        for ingredient in sample_ingredients:
            burger.add_ingredient(ingredient)
        
        expected_price = sum(ingredient.price for ingredient in sample_ingredients)
        assert burger.get_total_price() == expected_price

    def test_get_receipt(self, sample_ingredients):
        burger = Burger()
        for ingredient in sample_ingredients:
            burger.add_ingredient(ingredient)
        
        receipt = burger.get_receipt()
        assert isinstance(receipt, str)
        for ingredient in sample_ingredients:
            assert ingredient.name in receipt
        assert str(burger.get_total_price()) in receipt

    @patch('burger.Burger.get_total_price')
    def test_get_receipt_with_mocked_price(self, mock_get_total_price):
        mock_get_total_price.return_value = 350
        burger = Burger()
        receipt = burger.get_receipt()
        assert "350" in receipt
