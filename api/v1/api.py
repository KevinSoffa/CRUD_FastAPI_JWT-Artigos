from api.v1.endpoints import (artigo, usuario)
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(
    artigo.router, 
    prefix='/artigos', 
    tags=['artigos']
)

api_router.include_router(
    usuario.router, 
    prefix='/usuarios', 
    tags=['usuarios']
)
