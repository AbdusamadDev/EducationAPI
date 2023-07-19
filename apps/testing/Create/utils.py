import jwt
from environ import Env


def decode_jwt(token):
    try:
        env = Env()
        env.read_env()
        # Retrieve the secret key from the environment
        secret_key = env.str("SECRET_KEY")
        # Decode the JWT token
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_token
    except jwt.InvalidTokenError:
        # Handle invalid token
        print("Secret Key: ", secret_key)
        return None


if __name__ == "__main__":
    print(
        decode_jwt(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwMjEyOTkzLCJpYXQiOjE2ODk3ODA5OTMsImp0aSI6ImIyMWFkY2FlMWFmMzRjYjZhNDhlMzY1MDM4OWYzZjQ2IiwidXNlcl9pZCI6MX0.DuG-1B8Z1AGwJk799I9dy58d4rPSBNEGQlkqUy_kw70",
            "change",
        )
    )
