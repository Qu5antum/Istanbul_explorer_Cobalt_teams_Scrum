from sqlalchemy import DateTime, ForeignKey, Table, Column, UniqueConstraint
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

    comments: Mapped[list["Comment"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(nullable=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER, nullable=False)

    ratings: Mapped[list["PlaceRating"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    routes: Mapped[list["Route"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
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

    ratings: Mapped[list["PlaceRating"]] = relationship(
        back_populates="place",
        cascade="all, delete-orphan"
    )

    route_places: Mapped[list["RoutePlace"]] = relationship(
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

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="comments"
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )


class FavoritePlace(Base):
    __tablename__ = "favorite_places"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "place_id",
            name="uq_user_place_favorite"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )


class PlaceRating(Base):
    __tablename__ = "place_ratings"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "place_id",
            name="unique_user_place_rating"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    rating: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    place: Mapped["Place"] = relationship(
        back_populates="ratings"
    )

    user: Mapped["User"] = relationship(
        back_populates="ratings"
    )

    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )
    

class Route(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="routes"
    )

    title: Mapped[str] = mapped_column(nullable=False)
    total_distance: Mapped[float] = mapped_column(nullable=False)
    estimated_duration: Mapped[int] = mapped_column(nullable=False)
    share_token: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        unique=True,
    )
    is_public: Mapped[bool] = mapped_column(default=True)

    route_places: Mapped[list["RoutePlace"]] = relationship(
        back_populates="route",
        cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )


class RoutePlace(Base):
    __tablename__ = "route_places"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id", ondelete="CASCADE"),
        nullable=False
    )

    route: Mapped["Route"] = relationship(
        back_populates="route_places"
    )

    place_id: Mapped[int] = mapped_column(
        ForeignKey("places.id", ondelete="CASCADE"),
        nullable=False
    )

    place: Mapped["Place"] = relationship(
        back_populates="route_places"
    )

    order_number: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    arrival_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    departure_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    travel_duration: Mapped[int] = mapped_column(nullable=False)
    visit_duration: Mapped[int] = mapped_column(nullable=False)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.datetime.now(datetime.UTC), 
        index=True
    )