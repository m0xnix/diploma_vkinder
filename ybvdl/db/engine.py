from typing import Tuple

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ybvdl.db import Base
from ybvdl.db.models import User


def db_init(db_url: str, recreate: bool = True) -> Tuple[Engine, Session]:
    engine = create_engine(db_url, echo=True)

    if recreate:
        Base.metadata.create_all(engine)

    session = Session(engine)
    return (engine, session)
