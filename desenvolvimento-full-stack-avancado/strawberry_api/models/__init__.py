# from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
import asyncio
import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager
from typing import AsyncGenerator



# importando os elementos definidos no modelo
from models.base import Base
from models.produto import Produto
from models.comentario import Comentario

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite+aiosqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão assíncrona com o banco
engine = create_async_engine(
    db_url, 
    connect_args={"check_same_thread": False},
    echo=False
)

# Instancia um criador de seção com o banco
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()

async def _async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
