import jwt
from config import JWT_SECRET


def generate_jwt(email, password):
    return jwt.encode({"email": email, "password": password}, key=JWT_SECRET, algorithm="HS256")


def decode_jwt(jwt_token):
    return jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])
