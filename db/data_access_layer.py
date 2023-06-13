from typing import Sequence, Optional
from datetime import datetime

from fastapi import Depends, HTTPException, status
from sqlalchemy import text, Row
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db_session


class DataAccessLayer:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_salary(self, login: str) -> Row:
        get_salary_query = text('SELECT salary, increment_date FROM employees WHERE login = :login')
        salary = await self.session.execute(get_salary_query.bindparams(login=login))
        return salary.one()

    async def get_hashed_password_by_login(self, login: str) -> Optional[str]:
        query = text('SELECT hashed_password FROM employees WHERE login = :login')
        hashed_password = await self.session.execute(query.bindparams(login=login))
        row = hashed_password.one_or_none()
        if row:
            return row.hashed_password
        else:
            return None