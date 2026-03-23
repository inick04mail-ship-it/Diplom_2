import pytest
from helpers import create_order
from data import IngredientData, ErrorMessages


class TestCreateOrder:
    
    def test_create_order_with_auth_success(self, created_user):
        user_data, token = created_user
        order_data = {"ingredients": IngredientData.VALID_INGREDIENTS}
        response = create_order(order_data, token)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert "order" in response_data
    
    def test_create_order_without_auth_success(self):
        order_data = {"ingredients": IngredientData.VALID_INGREDIENTS}
        response = create_order(order_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert "order" in response_data
    
    def test_create_order_no_ingredients_fail(self, created_user):
        user_data, token = created_user
        order_data = {"ingredients": []}
        response = create_order(order_data, token)
        
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.NO_INGREDIENTS
    
    def test_create_order_invalid_hash_fail(self, created_user):
        user_data, token = created_user
        order_data = {"ingredients": [IngredientData.INVALID_HASH]}
        response = create_order(order_data, token)
        
        assert response.status_code == 500
    
    def test_create_order_one_ingredient_success(self, created_user):
        user_data, token = created_user
        order_data = {"ingredients": [IngredientData.BUN]}
        response = create_order(order_data, token)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True