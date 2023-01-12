from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from core.database import Session
from core.auth import oauth2_schema
from core.configs import settings
from models.usuario_model import UsuarioModel


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> Generator:
    sesseion: AsyncSession = Session()

    try:
        yield sesseion

    finally:
        await sesseion.close()

async def get_current_user(
    db: Session = Depends(get_session), 
    token: str = Depends(oauth2_schema)
    ) -> UsuarioModel:

    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial!',
        headers={"WWW-Authenticate": "Bearer"}
    )

    # Pega o Token e decodifica
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={'verify_aud': False}
        )
        username: str = payload.get("sub")

        if username is None:
            raise credential_exception

        # Montando o Token Data
        token_data: TokenData = TokenData(username=username)

    except JWTError:
        raise credential_exception


    # Buscando o usuário no banco de dados
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username))
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if usuario is None:
            raise credential_exception

        return usuario
