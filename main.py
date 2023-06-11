import uvicorn
from application import app

API_PORT: int = 8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=API_PORT)
