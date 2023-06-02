from api.schemas import TokenResponse, TokenRequest, SalaryRequest, SalaryResponse
from fastapi import FastAPI

router = FastAPI()

@router.post('/get_token', response_model=TokenResponse)
async def get_token(request: TokenRequest) -> TokenResponse:
    return TokenResponse(token=request.login)

@router.post('/get_salary', response_model=SalaryResponse)
async def get_salary(request: SalaryRequest) -> SalaryResponse:
    return SalaryResponse(salary='120', date_of_increase='30.05.2022')
