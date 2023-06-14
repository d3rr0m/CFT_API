from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from router import api_router
import settings

app = FastAPI()

@app.on_event("startup")
async def startup():
    engine = create_async_engine(settings.DB_PATH)
    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory

@app.on_event("shutdown")
async def shutdown():
    await app.state.db_engine.dispose()

app.include_router(router=api_router, prefix="/api")
