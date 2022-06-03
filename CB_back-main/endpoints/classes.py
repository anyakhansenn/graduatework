from typing import List
from pydantic import BaseModel, validator

class NewUser(BaseModel):
    login: str
    @validator('login')
    def is_acceptable(cls, v):
        if ' ' in v or '.' in v:
            raise ValueError('cannot contain non-acceptable letters')
        return v

class AuthUser(BaseModel):
    id: str
    @validator('id')
    def is_acceptable(cls, v):
        if ' ' in v or '.' in v:
            raise ValueError('cannot contain non-acceptable letters')
        return v

class Variant(BaseModel):
    direction: str
    variant: str

class UserMessage(BaseModel):
    id: str
    message: str
    variants: List[Variant]


class VariantMessage(BaseModel):
    id: str
    variant: str
    message: str