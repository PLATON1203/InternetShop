from pydantic import BaseModel, Field
from datetime import datetime
from .category import CategotyResponse
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1,max_length=200, 
                      description='Product name')
    descripthion: Optional[str] = Field(None, 
                                        description='Product description')
    price: float = Field(..., gt=0, description='Product price(must be greater than 0)')
    categoty_id:id =Field(..., description='Category ID')
    image_url: Optional[str] = Field(None, description='Product image URL')


class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(..., description='Unique product ID')
    name: str
    descripthion: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime 
    category: CategotyResponse = Field(..., description='Product category details')

    class Config:
        form_attributes = True


