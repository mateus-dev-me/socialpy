from fastapi import FastAPI

from .routes import main_router

app = FastAPI(
    title='Socialpy',
    version='0.1.0',
    description='Rede social baseada no twitter',
)


app.include_router(main_router)
