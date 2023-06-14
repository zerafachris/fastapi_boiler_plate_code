from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace the SQLite connection URL with your PostgreSQL connection URL
DATABASE_URL = "postgresql://postgres:root@localhost:5432/fastapi"

# Create a PostgreSQL engine instance
engine = create_engine(DATABASE_URL)

# Create declarative base meta instance
Base = declarative_base()

# Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
