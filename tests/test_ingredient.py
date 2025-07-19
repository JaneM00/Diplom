#test_ingredient.py
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE.SAUCE, "Соус традиционный галактический", 15),
        (INGREDIENT_TYPE.FILLING, "Говяжий метеорит (отбивная)", 3000),
        (INGREDIENT_TYPE.SAUCE, "", 0),
        (INGREDIENT_TYPE.FILLING, "Хрустящие минеральные кольца", -50)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE.SAUCE, "Соус традиционный галактический", 15)
        assert ingredient.get_type() == INGREDIENT_TYPE.SAUCE

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE.SAUCE, "Соус традиционный галактический", 15)
        assert ingredient.get_name() == "Соус традиционный галактический"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE.SAUCE, "Соус традиционный галактический", 15)
        assert ingredient.get_price() == 15
