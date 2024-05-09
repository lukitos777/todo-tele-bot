import asyncpg

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from configs import DB_CONFIGS

user = DB_CONFIGS['user']
password = DB_CONFIGS['password']
host = DB_CONFIGS['host']
port = DB_CONFIGS['port']
database = DB_CONFIGS['database']

DATABASE_URL =\
    f'postgresql+asyncpg://{user}:{password}' +\
    f'@{host}:{port}/{database}'

engine = create_async_engine(DATABASE_URL, echo=True)

# creating sessions to database to work with datadase
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)