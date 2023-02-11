from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from socialpy.utils.security import HashedPassword

if TYPE_CHECKING:
    from socialpy.db.models.post import Post


class User(SQLModel, table=True):
    """Represents the User Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword

    # It populates the .User attribute on the Post Model
    posts: List['Post'] = Relationship(back_populates='user')
