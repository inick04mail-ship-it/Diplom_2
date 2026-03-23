import pytest
from helpers import create_user, login_user
from data import UserData, ErrorMessages


class TestLoginUser:
    
    def test_login_existing_user_success(self):
        user_data = UserData.generate_user()
        create_user(user_data)
        
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = login_user(login_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert "accessToken" in response_data
    
    def test_login_wrong_password_fail(self):
        user_data = UserData.generate_user()
        create_user(user_data)
        
        login_data = {
            "email": user_data["email"],
            "password": "wrong_password"
        }
        response = login_user(login_data)
        
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.INCORRECT_LOGIN
    
    def test_login_wrong_email_fail(self):
        user_data = UserData.generate_user()
        create_user(user_data)
        
        login_data = {
            "email": "wrong@test.com",
            "password": user_data["password"]
        }
        response = login_user(login_data)
        
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.INCORRECT_LOGIN
    
    @pytest.mark.parametrize("missing_field", ["email", "password"])
    def test_login_missing_field_fail(self, missing_field):
        user_data = UserData.generate_user()
        create_user(user_data)
        
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        del login_data[missing_field]
        response = login_user(login_data)
        
        assert response.status_code == 401
        response_data = response.json()
        assert response_data["success"] is False