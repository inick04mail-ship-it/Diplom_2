import requests
from urls import BASE_URL, Endpoints

def create_user(user_data):
    """Создание пользователя"""
    return requests.post(f"{BASE_URL}{Endpoints.CREATE_USER}", json=user_data)

def login_user(login_data):
    """Авторизация пользователя"""
    return requests.post(f"{BASE_URL}{Endpoints.LOGIN_USER}", json=login_data)

def create_order(order_data, token=None):
    """Создание заказа (с токеном или без)"""
    headers = {}
    if token:
        if not token.startswith('Bearer '):
            token = f'Bearer {token}'
        headers = {"Authorization": token}
    
    return requests.post(
        f"{BASE_URL}{Endpoints.CREATE_ORDER}", 
        json=order_data, 
        headers=headers
    )

def delete_user(token):
    """Удаление пользователя"""
    headers = {"Authorization": token}
    return requests.delete(f"{BASE_URL}{Endpoints.CREATE_USER}", headers=headers)