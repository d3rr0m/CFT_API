from api.actions.get_token_by_login import get_token_by_login
from api.actions.check_token import check_is_valid_token
from api.schemas import TokenResponse, TokenRequest, SalaryRequest, SalaryResponse
from fastapi import FastAPI, HTTPException, status

router = FastAPI()

@router.post('/get_token', response_model=TokenResponse)
async def get_token(request: TokenRequest) -> TokenResponse:
    token=get_token_by_login(request.login, request.password)
    if token:
        return TokenResponse(token)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='The username and password did not match.',
            headers={'WWW-Authentication': 'Bearer'}
        )

@router.post('/get_salary', response_model=SalaryResponse)
async def get_salary(request: SalaryRequest) -> SalaryResponse:
    if check_is_valid_token(request.token):
        return SalaryResponse(salary='120', date_of_increase='30.05.2022')
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='The token has expired or does not exist',
            headers={'WWW-Authentication': 'Bearer'}
        )
