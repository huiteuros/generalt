from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import hashlib

security = HTTPBasic()

def get_authorized_users():
    with open("auth.txt", "r") as f:
        users = [line.strip().split(":") for line in f if ":" in line]
    return users


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    users = get_authorized_users()
    if [credentials.username, hashlib.sha256(credentials.password.encode('utf-8')).hexdigest()] in users:
        return credentials.username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Identifiants invalides",
        headers={"WWW-Authenticate": "Basic"},
    )
