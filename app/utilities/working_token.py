from config import SECRET_KEY
import jwt


ALGORITHM = 'HS256'


def get_token(data: dict) -> str:
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_data_from_token(token) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
