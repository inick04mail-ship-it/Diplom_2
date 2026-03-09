import pytest
from data import UserData
from helpers import create_user, delete_user

@pytest.fixture
def created_user():
    """Фикстура создает пользователя и возвращает его данные + токен"""
    user_data = UserData.generate_user()
    response = create_user(user_data)
    
    token = None
    if response.status_code == 200:
       
        token = response.json().get("accessToken")
    
    yield user_data, token
    
    
    if token:
        delete_user(token)