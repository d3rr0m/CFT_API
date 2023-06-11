from typing import Sequence

from fastapi import Depends
from sqlalchemy import text
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
