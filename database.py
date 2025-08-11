from sqlalchemy import create_engine  #connection manager
from sqlalchemy.orm import sessionmaker #session is a temporary workspace where you can perform database operations
from sqlalchemy.ext.declarative import declarative_base
#Think of create_engine as setting up a phone line to the database, sessionmaker as a notepad where you jot down changes before saving them, and declarative_base as a blueprint for creating database table structures.

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()