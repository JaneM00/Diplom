# test_burger.py

import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientType


class TestBurger:
    def test_set_buns(self):
        """Проверяет установку булочки для бургера"""
        burger = Burger()
        bun = Bun("Краторная булка", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        """Проверяет добавление ингредиента в бургер"""
        burger = Burger()
        ingredient = Ingredient(IngredientType.SAUCE, "Соус", 50)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        """Проверяет удаление ингредиента из бургера"""
        burger = Burger()
        ingredient1 = Ingredient(IngredientType.SAUCE, "Соус1", 50)
        ingredient2 = Ingredient(IngredientType.FILLING, "Начинка", 100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        """Проверяет перемещение ингредиента в бургере"""
        burger = Burger()
        ingredient1 = Ingredient(IngredientType.SAUCE, "Соус", 50)
        ingredient2 = Ingredient(IngredientType.FILLING, "Начинка", 100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        """Проверяет расчет стоимости бургера"""
        burger = Burger()
        bun = Bun("Булка", 100)
        ingredient1 = Ingredient(IngredientType.SAUCE, "Соус", 50)
        ingredient2 = Ingredient(IngredientType.FILLING, "Начинка", 100)
        
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        expected_price = bun.get_price() * 2 + ingredient1.get_price() + ingredient2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        """Проверяет формирование чека для бургера"""
        burger = Burger()
        bun = Bun("Краторная булка", 100)
        ingredient1 = Ingredient(IngredientType.SAUCE, "Острый соус", 50)
        ingredient2 = Ingredient(IngredientType.FILLING, "Котлета", 100)
        
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        expected_receipt = (
            "(==== Краторная булка ====)\n"
            "= sauce Острый соус =\n"
            "= filling Котлета =\n"
            "(==== Краторная булка ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        
        assert burger.get_receipt() == expected_receipt

    def test_empty_burger_price(self):
        """Проверяет расчет стоимости бургера без ингредиентов"""
        burger = Burger()
        bun = Bun("Булка", 100)
        burger.set_buns(bun)
        assert burger.get_price() == bun.get_price() * 2
