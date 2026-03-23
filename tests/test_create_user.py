import requests
import pytest
from urls import BASE_URL, Endpoints
from data import UserData, ErrorMessages


class TestCreateUser:
    
    def test_create_unique_user_success(self):
        user_data = UserData.generate_user()
        response = requests.post(f"{BASE_URL}{Endpoints.CREATE_USER}", json=user_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]
        assert "accessToken" in response_data
        
        access_token = response_data.get("accessToken")
        if access_token:
            headers = {"Authorization": access_token}
            requests.delete(f"{BASE_URL}{Endpoints.CREATE_USER}", headers=headers)
    
    def test_create_existing_user_fail(self):
        user_data = UserData.generate_user()
        create_response = requests.post(f"{BASE_URL}{Endpoints.CREATE_USER}", json=user_data)
        access_token = create_response.json().get("accessToken")
        
        response = requests.post(f"{BASE_URL}{Endpoints.CREATE_USER}", json=user_data)
        
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.USER_EXISTS
        
        if access_token:
            headers = {"Authorization": access_token}
            requests.delete(f"{BASE_URL}{Endpoints.CREATE_USER}", headers=headers)
    
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_fail(self, missing_field):
        user_data = UserData.generate_user()
        del user_data[missing_field]
        
        response = requests.post(f"{BASE_URL}{Endpoints.CREATE_USER}", json=user_data)
        
        assert response.status_code == 403
        response_data = response.json()
        assert response_data["success"] is False
        assert response_data["message"] == ErrorMessages.REQUIRED_FIELDS