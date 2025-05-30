from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Block(Base):
    __tablename__ = "blocks"
    number = Column(Integer, primary_key=True)
    hash = Column(String, unique=True, nullable=False)
    timestamp = Column(DateTime, nullable=False)


def get_engine(db_path: str):
    return create_engine(f"sqlite:///{db_path}")


def init_db(engine):
    Base.metadata.create_all(engine)


def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
