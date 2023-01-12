from core.configs import settings
from api.v1.api import api_router
from fastapi import FastAPI


app = FastAPI(title='FastAPI | PostgreSQL e JWT - Segurança - Kevin Soffa')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__=='__main__':
    import uvicorn

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_level='info',
        reload=True
    )


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc0MTYwODcwLCJpYXQiOjE2NzM1NTYwNzAsInN1YiI6IjcifQ.qPyHgWLl6MNmhe3fHUEvAK_t9-5eb6nHJA4n4TMEEMA
Tipo: bearer


Token (kevin@gmail.com)
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc0MTYyNDkxLCJpYXQiOjE2NzM1NTc2OTEsInN1YiI6IjEifQ.2D_AXb7TqYOE9e3gVT3CHUW7Une7TfXYh1Fzi-Nkxwc
"""