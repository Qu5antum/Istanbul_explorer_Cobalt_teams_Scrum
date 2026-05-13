from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .base_repository import BaseRepository
from src.database.models import Comment

class CommentRepository(BaseRepository):
    model = Comment

    async def get_comments_by_place_id(self, place_id: int):
        result = await self.session.execute(
            select(self.model)
            .options(selectinload(self.model.place))
            .where(self.model.place_id == place_id)
        )

        return result.scalars().all()