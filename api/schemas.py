from pydantic import BaseModel


class TokenRequest(BaseModel):
    login: str
    password: str


class TokenResponse(BaseModel):
    token: str


class SalaryRequest(BaseModel):
    token: str


class SalaryResponse(BaseModel):
    salary: float
    increment_date: str