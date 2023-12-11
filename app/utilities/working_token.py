import jwt
from jwt import DecodeError
from config import SECRET_KEY


class WorkingWithToken:
    __algoritm = 'HS256'

    def get_token(self, data: dict) -> str:
        return jwt.encode(data, SECRET_KEY, algorithm=self.__algoritm)

    def get_data_from_token(self, token: str) -> dict:

        decoded_token: dict = {}

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=self.__algoritm)
            return decoded_token
        except DecodeError:
            return decoded_token