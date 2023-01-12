from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.__all__models
    print('=='*10)
    print('Criando as tabelas no banco')
    print('=='*10)

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBasemodel.metadata.drop_all)
        await conn.run_sync(settings.DBBasemodel.metadata.create_all)

    print('=='*10)
    print('Tabelas criadas com sucesso!')
    print('=='*10)


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
