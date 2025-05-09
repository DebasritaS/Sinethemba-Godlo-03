from pydantic import BaseModel
from typing import List

class User(BaseModel):
    user_id: str
    name: str
    email: str
    roles: List[str]

class UserCreateRequest(BaseModel):
    user_id: str
    name: str
    email: str
    roles: List[str]

class UserResponse(BaseModel):
    user_id: str
    name: str
    email: str
    roles: List[str]
