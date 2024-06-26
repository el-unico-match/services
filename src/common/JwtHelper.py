import jwt
from datetime import datetime, timedelta, timezone
from configs.settings import settings

def createToken(id: str, baseUrl: str, type: str):
    payload = {
        'id': id,
        'baseUrl': baseUrl,
        'type': type,
        'exp': datetime.now(timezone.utc) + timedelta(days=90)
    }

    secret_key = settings.jwt_private_key
    algorithm = settings.jwt_algorithm

    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    return token