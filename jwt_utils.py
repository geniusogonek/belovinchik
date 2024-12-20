import jwt

from config import JWT_SECRET


def generate_jwt(email, password):
    return jwt.encode({"email": email, "password": password}, key=JWT_SECRET, algorithm="HS256")


def decode_jwt(jwt_token):
    try:
        is_auth = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])
    except Exception as e:
        print(e)
        return False
    return is_auth