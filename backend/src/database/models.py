from sqlalchemy import DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum
import uuid
import datetime

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class Base(DeclarativeBase):
    pass



place_category = Table(
    "place_category",
    Base.metadata,

    Column(
        "place_id",
        ForeignKey("places.id", ondelete="CASCADE"),
        primary_key=True
    ),

    Column(
        "category_id",
        ForeignKey("categories.id", ondelete="CASCADE"),
        primary_key=True
    ),
)

    
class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(nullable=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER, nullable=False)
    
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)

    places: Mapped[list["Place"]] = relationship(
        secondary=place_category,
        back_populates="categories",
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )


class Place(Base):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[str] = mapped_column(nullable=True)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    image_path: Mapped[str] = mapped_column(nullable=False)

    categories: Mapped[list["Category"]] = relationship(
        secondary=place_category,
        back_populates="places",
    )

    comments: Mapped[list["Comment"]] = relationship(
        back_populates="place",
        cascade="all, delete-orphan"
    )
 
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)

    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id")
    )

    place: Mapped["Place"] = relationship(
        back_populates="comments"
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )

