# test_database.py
import pytest
from unittest.mock import Mock, patch
from praktikum.database import Database


class TestDatabase:
    @patch('praktikum.database.Database')
    def test_available_buns(self, mock_db):
        mock_db.available_buns.return_value = [
            Mock(get_name=lambda: "Краторная булка"), 
            Mock(get_name=lambda: "Флюоресцентная булка")
        ]
        
        buns = mock_db.available_buns()
        assert len(buns) == 2
        assert buns[0].get_name() == "Краторная булка"
        assert buns[1].get_name() == "Флюоресцентная булка"

    @patch('praktikum.database.Database')
    def test_available_ingredients(self, mock_db):
        mock_db.available_ingredients.return_value = [
            Mock(get_name=lambda: "Соус Spicy-X"),
            Mock(get_name=lambda: "Мясо бессмертных моллюсков")
        ]
        
        ingredients = mock_db.available_ingredients()
        assert len(ingredients) == 2
        assert ingredients[0].get_name() == "Соус Spicy-X"
        assert ingredients[1].get_name() == "Мясо бессмертных моллюсков"
