import pytest
from helpers import create_user
from data import UserData, ErrorMessages


class TestCreateUser:
    
    def test_create_unique_user_success(self):
        user_data = UserData.generate_user()
        response = create_user(user_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]
        assert "accessToken" in response_data
    
    def test_create_existing_user_fail(self):
        user_data = UserData.generate_user()
        create_user(user_data)
        response = create_user(user_data)
        
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.USER_EXISTS
    
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_fail(self, missing_field):
        user_data = UserData.generate_user()
        del user_data[missing_field]
        response = create_user(user_data)
        
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.REQUIRED_FIELDS