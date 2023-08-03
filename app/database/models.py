from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Table, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    ...


Like = Table(
    'likes',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('created_at', DateTime, server_default=func.now()),
)

Share = Table(
    'shares',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('created_at', DateTime, server_default=func.now()),
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    avatar: Mapped[str | None]
    bio: Mapped[str | None]
    password: Mapped[str]

    posts: Mapped[list[Post]] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )

    post_like: Mapped[list[Post]] = relationship(
        secondary=Like,
        back_populates='user_like',
    )

    post_share: Mapped[list[Post]] = relationship(
        secondary=Share,
        back_populates='user_share',
    )

    def __repr__(self):
        return f"""
        User(username={self.username}, email={self.email}, bio={self.bio})
        """


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='posts')

    user_like: Mapped[list[User]] = relationship(
        secondary=Like, back_populates='post_like'
    )

    user_share: Mapped[list[User]] = relationship(
        secondary=Share,
        back_populates='post_share',
    )

    def __repr__(self):
        return f'Post(text={self.text}, date={self.created_at})'

    def __lt__(self, other):
        """This enables post.replies.sort() to sort by date"""
        return self.created_at < other.create_at
