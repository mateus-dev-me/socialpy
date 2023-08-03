from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.ECHO)


def get_session():
    with Session(engine) as session:
        yield session
