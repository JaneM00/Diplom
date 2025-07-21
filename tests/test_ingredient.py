# test_ingredient.py
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_ingredient_initialization_sauce(self):
        """Проверяет корректность инициализации ингредиента-соуса"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100

    def test_ingredient_initialization_filling(self):
        """Проверяет корректность инициализации ингредиента-начинки"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
        assert ingredient.type == INGREDIENT_TYPE_FILLING
        assert ingredient.name == "cutlet"
        assert ingredient.price == 200

    def test_get_type(self):
        """Проверяет метод get_type()"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_name(self):
        """Проверяет метод get_name()"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 300)
        assert ingredient.get_name() == "dinosaur"

    def test_get_price(self):
        """Проверяет метод get_price()"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 250)
        assert ingredient.get_price() == 250

    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "", 0),
        (INGREDIENT_TYPE_FILLING, "Very long name" * 10, -100),
        ("UNKNOWN_TYPE", "special", 999)
    ])
    def test_edge_cases(self, ingredient_type, name, price):
        """Проверяет крайние случаи при инициализации ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price
