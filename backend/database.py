from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_"}
)