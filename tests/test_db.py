from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import Post, User


def test_create_user_db(session: Session):
    user = User(username='mateus', email='mateus@gmail.com', password='1234')
    session.add(user)
    session.commit()

    user_db = session.scalar(select(User).where(User.id == user.id))
    assert user.username == user_db.username


def test_create_post_db(session: Session):
    user = User(
        username='mateus',
        email='mateus@gmail.com',
        password='1234',
        posts=[Post(text='test post')],
    )
    session.add(user)
    session.commit()

    post = session.scalar(select(Post).where(Post.user_id == user.id))
    assert post in user.posts
