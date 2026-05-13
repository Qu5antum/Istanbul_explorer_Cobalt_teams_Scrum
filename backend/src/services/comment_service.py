from sqlalchemy.exc import IntegrityError

from src.database.db import AsyncSession
from src.repositories.comment_repository import CommentRepository
from src.repositories.place_repository import PlaceRepository
from src.exception_handlers.place_exception import PlaceNotFoundException
from src.exception_handlers.db_exception import DatabaseException


class CommentService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.comment_repo = CommentRepository(session=self.session)
        self.place_repo = PlaceRepository(session=self.session)

    # Yorum ekleme metodu
    async def create_comment(self, title: str, place_id: int):
        place = await self.place_repo.get(id=place_id)

        if not place:
            raise PlaceNotFoundException("Konum bulunmadı")
        
        try:
            new_comment = await self.comment_repo.create(
                title=title,
                place_id=place_id
            )

            await self.session.commit()
            await self.session.refresh(new_comment)
        except IntegrityError:
            raise DatabaseException("Veritaban hatası")
        
        return {"detail": "Yorum eklendi"}
    
    # Konuma göre yorumları alma
    async def get_all_comment_by_place(self, place_id):
        place = await self.place_repo.get(id=place_id)

        if not place:
            return PlaceNotFoundException("Konum bulunmadı")
        
        comments = await self.comment_repo.get_comments_by_place_id(place_id=place_id)

        return comments
        


        

        

