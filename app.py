from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str


@app.post('/user/')
def set_username(user: User):
    return {'key': user}


@app.get('/')
def main():
    return {'key': 'value'}
