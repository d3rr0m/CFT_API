import uvicorn

from application import app
import settings

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=settings.API_PORT)
