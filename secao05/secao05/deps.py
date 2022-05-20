from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from secao05.database import Session


async def get_session() -> Generator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()   
    