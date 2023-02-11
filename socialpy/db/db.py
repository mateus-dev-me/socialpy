from fastapi import Depends
from sqlmodel import Session, create_engine

from socialpy.config import settings

engine = create_engine(
    settings.db.uri,
    echo=settings.db.echo,
)


def get_session():
    with Session(engine) as session:
        yield session


ActiveSession = Depends(get_session)
