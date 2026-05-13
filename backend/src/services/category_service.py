from sqlalchemy.exc import IntegrityError

from src.database.db import AsyncSession
from src.api.schemas.category_schema import CategoryCreate
from src.repositories.category_repository import CategoryRepository
from src.exception_handlers.db_exception import DatabaseException
from src.exception_handlers.category_exception import CategoryAlreadyExists


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.category_repo = CategoryRepository(session=self.session)
    
    # Kategori oluşturma
    async def create_category(self, category: CategoryCreate) -> dict[str, str]:
        existing_category = await self.category_repo.get_title(title=category.title)

        if existing_category:
            raise CategoryAlreadyExists("Kategori zaten var")
        
        try:
            new_category = await self.category_repo.create(
                title=category.title
            )

            await self.session.commit()
            await self.session.refresh(new_category)
        except IntegrityError:
            raise DatabaseException("Veritaban hatası")
        
        return {"detail": "Kategori başarıyla oluşturuldu"}
    
    # Veritabandan kategorileri çekme
    async def get_categories(self):
        categories = await self.category_repo.get_all()

        return categories
