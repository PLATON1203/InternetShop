from sqlalchemy import Column, Intenger, String
from sqlalchemy.orm import relathionship
from ..database import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Intenger, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)

    products = relathionship('Product', back_populates='category')

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"