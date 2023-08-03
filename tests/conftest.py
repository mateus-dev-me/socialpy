import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.models import Base, Post, User


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def user(session):
    user = User(
        username='teste', email='teste@example.com', password='testepassword'
    )
    session.add(user)
    session.commit()
    return user


@pytest.fixture
def post(session):
    user = User(
        username='teste2', email='teste2@example.com', password='testepassword'
    )
    post = Post(text='teste post', user_id=user.id)

    session.add_all([user, post])
    session.commit()

    return post
