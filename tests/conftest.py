import asyncio
import os
from datetime import timedelta
from typing import Any
from typing import Generator

import pytest
from starlette.testclient import TestClient

from api.handlers import router
#from security import create_access_token

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="function")
async def client() -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    with TestClient(router) as client:
        yield client
