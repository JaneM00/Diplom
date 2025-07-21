# data.py
from faker import Faker

fake = Faker()

class TestData:
    @staticmethod
    def random_user():
        return {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
    
    @staticmethod
    def valid_ingredients():
        return ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    
    @staticmethod
    def invalid_ingredients():
        return ["invalid_hash_123", "wrong_hash_456"]
