from controller.get_token_by_login import verify_password, get_token_by_login
from controller.check_token import check_is_valid_token
from api.schemas import TokenResponse, TokenRequest, SalaryRequest, SalaryResponse
from fastapi import HTTPException, status, APIRouter, Depends

from db.data_access_layer import DataAccessLayer

import settings
router = APIRouter()


@router.post('/token', response_model=TokenResponse)
async def get_token(
    request: TokenRequest,
    data_access_layer: DataAccessLayer = Depends()) -> TokenResponse:
    """Get employee token."""
    hashed_password = await data_access_layer.get_hashed_password_by_login(request.login)
    
    if not hashed_password:
       raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Login not found',
            headers={'WWW-Authentication': 'Bearer'}
        ) 

    if not verify_password(request.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='The password and login did not match',
            headers={'WWW-Authentication': 'Bearer'}
        )
    
    token=get_token_by_login(request.login, settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    #get_token_by_login(request.login, request.password)
    #if token:
    return TokenResponse(token=token)


@router.post('/salary', response_model=SalaryResponse)
async def get_salary(
    request: SalaryRequest,
    data_access_layer: DataAccessLayer = Depends(),
) -> SalaryResponse:
    """Get employee salary and next date of increment"""
    # if check_is_valid_token(request.token):
    all_employees = await data_access_layer.get_all_employees()
    a = check_is_valid_token(request.token)
    return SalaryResponse(
        salary='120',
        date_of_increase='30.05.2022',
        all=all_employees,
        login=a[0],
        exp=a[1]
    )
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail='The token has expired or does not exist',
    #         headers={'WWW-Authentication': 'Bearer'}
    #     )
