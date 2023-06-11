from controller.get_token_by_login import get_token_by_login
from api.schemas import TokenResponse, TokenRequest, SalaryRequest, SalaryResponse
from fastapi import HTTPException, status, APIRouter, Depends

from db.data_access_layer import DataAccessLayer

router = APIRouter()


@router.post('/get_token', response_model=TokenResponse)
async def get_token(request: TokenRequest) -> TokenResponse:
    """Get employee token."""
    token = get_token_by_login(request.login, request.password)
    if token:
        return TokenResponse(token=token)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='The username and password did not match.',
            headers={'WWW-Authentication': 'Bearer'}
        )


@router.post('/get_salary', response_model=SalaryResponse)
async def get_salary(
    request: SalaryRequest,
    data_access_layer: DataAccessLayer = Depends(),
) -> SalaryResponse:
    # if check_is_valid_token(request.token):
    all_employees = await data_access_layer.get_all_employees()
    return SalaryResponse(
        salary='120',
        date_of_increase='30.05.2022',
        all=all_employees,
    )
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail='The token has expired or does not exist',
    #         headers={'WWW-Authentication': 'Bearer'}
    #     )
