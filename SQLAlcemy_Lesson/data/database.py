from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

_session = None


class Base(DeclarativeBase):
    pass


def init():
    global _session
    # https://python.org
    engine = create_engine("sqlite+pysqlite:///shop_test1.db", echo=True)
    _session = sessionmaker(bind=engine)
    from . import __all_models
    Base.metadata.create_all(engine)


def create_session() -> Session:
    global _session
    if _session is None:
        raise Exception("Не инициализовано!")
    return _session()
