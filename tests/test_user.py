import pytest
import random
from sqlalchemy.orm import Session
from .test_db import get_test_db
from app.users.crud import create_user, delete_user, get_users, get_user
from app.users.schemas import UserCreate, UserInDBBase


@pytest.fixture
def test_db():
    for db in get_test_db():
        yield db


CHARS = "abcdefghijklmnopqrstuvwxyz1234567890"


def random_email():
    email = "".join(random.choices(CHARS, k=8)) + "@example.com"
    return email


def random_username():
    username = "".join(random.choices(CHARS, k=8))
    return username


def random_user():
    return UserCreate(username=random_username(), email=random_email(), password='Password123!')


def test_create_user(test_db: Session):
    user_data = random_user()
    user = create_user(db=test_db, user=user_data)

    assert user.username == user_data.username
    assert user.email == user_data.email


def get_random_user_id(db: Session = None):
    users = get_users(db)
    return random.choice([user.id for user in users])


def test_delete_user(test_db: Session):
    new_user = random_user()
    created_user = create_user(db=test_db, user=new_user)
    deleted_user = delete_user(db=test_db, user_id=created_user.id)
    assert deleted_user.id == created_user.id
    assert get_user(db=test_db, user_id=created_user.id) is None
