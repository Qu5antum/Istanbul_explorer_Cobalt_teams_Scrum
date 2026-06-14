import uuid
from datetime import datetime, timezone

import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.database.models import Category, Place

BASE_API = "/api"

TEST_DB_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(TEST_DB_URL, echo=False)
AsyncTestSession = async_sessionmaker(bind=engine, expire_on_commit=False)


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


async def get_model_id(model, **filters):
    async with AsyncTestSession() as session:
        result = await session.execute(select(model).filter_by(**filters))
        instance = result.scalar_one_or_none()
        return instance.id if instance else None


async def register_user(client: AsyncClient, role: str = "user") -> tuple[str, str]:
    email = f"test-{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123!"
    payload = {
        "email": email,
        "phone_number": "+905555555555",
        "password": password,
        "role": role,
    }

    response = await client.post(f"{BASE_API}/user/register", json=payload)
    assert response.status_code == 201, response.text
    return email, password


async def login_user(client: AsyncClient, email: str, password: str) -> str:
    response = await client.post(
        f"{BASE_API}/user/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == 201, response.text

    payload = response.json()
    assert "access_token" in payload
    return payload["access_token"]


async def create_category(client: AsyncClient, token: str, title: str) -> int:
    response = await client.post(
        f"{BASE_API}/admin/category/create",
        json={"title": title},
        headers=auth_headers(token),
    )
    assert response.status_code == 201, response.text

    category_id = await get_model_id(Category, title=title)
    assert category_id is not None
    return category_id


async def create_place(client: AsyncClient, token: str, category_id: int, title: str) -> int:
    payload = {
        "title": title,
        "link": "https://example.com",
        "price": "Free",
        "latitude": 41.0082,
        "longitude": 28.9784,
        "address": "Istanbul, Turkey",
        "description": "Test location description",
        "image_path": "images/test.jpg",
        "category_ids": [category_id],
    }

    response = await client.post(
        f"{BASE_API}/admin/place/create",
        json=payload,
        headers=auth_headers(token),
    )
    assert response.status_code == 201, response.text

    place_id = await get_model_id(Place, title=title)
    assert place_id is not None
    return place_id


@pytest.mark.asyncio
async def test_user_register_and_login(client: AsyncClient):
    email, password = await register_user(client)
    token = await login_user(client, email, password)

    assert token


@pytest.mark.asyncio
async def test_admin_create_place_and_user_comment_rate_flow(client: AsyncClient):
    admin_email, admin_password = await register_user(client, role="admin")
    admin_token = await login_user(client, admin_email, admin_password)

    category_title = f"Category {uuid.uuid4().hex[:6]}"
    category_id = await create_category(client, admin_token, category_title)

    place_title = f"Place {uuid.uuid4().hex[:6]}"
    place_id = await create_place(client, admin_token, category_id, place_title)

    regular_email, regular_password = await register_user(client, role="user")
    regular_token = await login_user(client, regular_email, regular_password)

    comment_response = await client.post(
        f"{BASE_API}/place/{place_id}/comment/create/",
        json={"title": "Test comment"},
        headers=auth_headers(regular_token),
    )
    assert comment_response.status_code == 201, comment_response.text
    assert comment_response.json()["detail"] == "Yorum eklendi"

    comment_list_response = await client.get(
        f"{BASE_API}/place/{place_id}/comment/",
        headers=auth_headers(regular_token),
    )
    assert comment_list_response.status_code == 200, comment_list_response.text

    comments = comment_list_response.json()
    assert isinstance(comments, list)
    assert len(comments) == 1
    assert comments[0]["title"] == "Test comment"
    assert comments[0]["user"]["email"] == regular_email

    rating_response = await client.post(
        f"{BASE_API}/place/{place_id}/rate",
        json={"rating": 5},
        headers=auth_headers(regular_token),
    )
    assert rating_response.status_code == 201, rating_response.text
    assert rating_response.json()["detail"] == "Değerlendirme başarıyla bıraktınız"

    place_rating_response = await client.get(
        f"{BASE_API}/place/{place_id}/rating",
        headers=auth_headers(regular_token),
    )
    assert place_rating_response.status_code == 200, place_rating_response.text

    rating_payload = place_rating_response.json()
    assert rating_payload["average_rating"] == 5.0
    assert rating_payload["total_reviews"] == 1

    place_detail_response = await client.post(
        f"{BASE_API}/place/{place_id}",
        json={"lat": 41.0082, "lng": 28.9784},
        headers=auth_headers(admin_token),
    )
    assert place_detail_response.status_code == 200, place_detail_response.text

    place_data = place_detail_response.json()
    assert place_data["id"] == place_id
    assert place_data["title"] == place_title
    assert place_data["description"] == "Test location description"
    assert "distance" in place_data
