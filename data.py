import random
import string

class UserData:
    @staticmethod
    def generate_user():
        email = f"test_user_{random.randint(100, 999)}@test.com"
        password = "".join(random.choices(string.ascii_letters, k=8))
        name = f"User_{random.randint(100, 999)}"
        return {
            "email": email,
            "password": password,
            "name": name
        }

class IngredientData:
    
    BUN = '61c0c5a71d1f82001bdaaa6d'  # ФЛЮОРЕСЦЕНТНАЯ БУЛКА R2-D3
    
    
    SAUCE = '61c0c5a71d1f82001bdaaa72'  # СОУС SPICY-X
    
    
    FILLING = '61c0c5a71d1f82001bdaaa6f'  # МЯСО БЕССМЕРТНЫХ МОЛЛЮСКОВ PROTOSTOMIA
    
   
    VALID_INGREDIENTS = [
        '61c0c5a71d1f82001bdaaa6d',  # булка
        '61c0c5a71d1f82001bdaaa72',  # соус
        '61c0c5a71d1f82001bdaaa6f',  # начинка
    ]
    
    INVALID_HASH = "invalid_hash_123"

class ErrorMessages:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    INCORRECT_LOGIN = "email or password are incorrect"
    NO_INGREDIENTS = "Ingredient ids must be provided"