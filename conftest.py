# conftest.py
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Фикстуры для тестов Bun
@pytest.fixture
def sample_bun():
    """Возвращает тестовую булочку"""
    return Bun("Краторная булка N-200i", 1255)


@pytest.fixture
def another_bun():
    """Возвращает другую тестовую булочку"""
    return Bun("Флюоресцентная булка R2-D3", 988)


# Фикстуры для тестов Ingredient
@pytest.fixture
def sauce_ingredient():
    """Возвращает тестовый соус"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)


@pytest.fixture
def filling_ingredient():
    """Возвращает тестовую начинку"""
    return Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)


# Фикстуры для тестов Burger
@pytest.fixture
def empty_burger():
    """Возвращает пустой бургер"""
    return Burger()


@pytest.fixture
def prepared_burger(sample_bun, sauce_ingredient, filling_ingredient):
    """Возвращает бургер с подготовленными ингредиентами"""
    burger = Burger()
    burger.set_buns(sample_bun)
    burger.add_ingredient(sauce_ingredient)
    burger.add_ingredient(filling_ingredient)
    return burger


# Фикстуры для тестов Database
@pytest.fixture
def database():
    """Возвращает инициализированную базу данных"""
    return Database()


@pytest.fixture
def database_buns(database):
    """Возвращает булочки из базы данных"""
    return database.available_buns()


@pytest.fixture
def database_ingredients(database):
    """Возвращает ингредиенты из базы данных"""
    return database.available_ingredients()


# Общие фикстуры
@pytest.fixture
def sample_ingredients(sauce_ingredient, filling_ingredient):
    """Возвращает список тестовых ингредиентов"""
    return [sauce_ingredient, filling_ingredient]


@pytest.fixture
def sample_buns(sample_bun, another_bun):
    """Возвращает список тестовых булочек"""
    return [sample_bun, another_bun]
