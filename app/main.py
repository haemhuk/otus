# site-packages
import uvicorn
from fastapi import FastAPI

# project
from config import load_config


config, secret = load_config()
app = FastAPI()


@app.get('/')
async def root():
    return {'hostname': config['HOSTNAME']}


@app.get('/config')
async def configuration():
    return dict([(key, value) for key, value in config.items()])


@app.get('/health')
async def health():
    return {'status': 'OK'}


@app.get('/version')
async def version():
    return {'version': config['VERSION']}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
