from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/robot_order", max_overflow=5)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


class Robot(Base):

    __tablename__ = "robot"
    uuid = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(20))
    total_power = Column(Integer)
    portable_package = Column(Integer)


DBSession = sessionmaker(bind=engine)
init_db()