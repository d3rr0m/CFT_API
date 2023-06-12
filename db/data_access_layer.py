from typing import Sequence, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy import text, Result
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db_session


class DataAccessLayer:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_all_employees(self) -> Sequence:
        query = """
            SELECT * FROM employees
        """
        employees = await self.session.execute(text(query))

        return employees.mappings().all()

    async def get_hashed_password_by_login(self, login: str) -> Optional[str]:
        query = text('select hashed_password from employees where login = :login')
        hashed_password = await self.session.execute(query.bindparams(login=login))
        row = hashed_password.one_or_none()
        if row:
            return row.hashed_password
        else:
            return None
            