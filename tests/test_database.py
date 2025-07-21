# test_database.py
import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        """Проверяет получение списка доступных булочек"""
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_available_ingredients(self):
        """Проверяет получение списка доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        # Проверяем соусы
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200
        
        # Проверяем начинки
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
        
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200

    def test_database_initialization(self):
        """Проверяет корректность инициализации базы данных"""
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6
        assert isinstance(db.buns[0], Bun)
        assert isinstance(db.ingredients[0], Ingredient)
