from sqlalchemy import create_engine,DateTime
from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped,MappedAsDataclass,mapped_column
from datetime import datetime
from sqlalchemy.sql import func
from dotenv import load_dotenv
import os

load_dotenv()

DATBASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(
    DATBASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)


SessionaLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


class CreateAtMixin:
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False,init=False) 

class TimeMixin:
    update_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False,init=False)    

class Base(MappedAsDataclass,DeclarativeBase,kw_only=True):
    pass