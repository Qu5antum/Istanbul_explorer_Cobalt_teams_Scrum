from abc import ABC, abstractmethod
from sqlalchemy import select
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

# Veritabanı ile çalışma ana sınıfı
class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, data: dict):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get_object_by_id(self, id: int):
        raise NotImplementedError
    

class BaseRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, **kwargs):
        try:
            new_object = self.model(**kwargs)  
            self.session.add(new_object)
            await self.session.commit()
            await self.session.refresh(new_object)

            return new_object
        except:
            await self.session.rollback()
            raise
    
    async def get_all(self):
        result = await self.session.execute(
            select(self.model)
        )

        return result.scalars().all()
    
    async def get_object_by_id(self, id: int):
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )

        return result.scalar_one_or_none()
        