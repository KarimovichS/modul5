from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://postgres:1@localhost/ss", echo=True)

Base = declarative_base()
metadata = Base.metadata
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'user_r'
    id = Column(Integer, primary_key=True)
    user_telegram_id = Column(String, unique=True)
    username = Column(String)
    created = Column(DateTime)



class Message_(Base):
    __tablename__ = 'usermessage'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    text = Column(String)
    created = Column(DateTime)


Base.metadata.create_all(engine)
