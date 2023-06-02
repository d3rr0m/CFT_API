import uvicorn
from typing import Union
from fastapi import FastAPI

from api.handlers import router

API_PORT: int = 8000

if __name__=='__main__':
    uvicorn.run(router, host='127.0.0.1', port=API_PORT)