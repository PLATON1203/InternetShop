from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(...,min_length=5, max_length=100,
                      description="Category name")
    slug: str = Field(..., min_length=5, max_length=100,
                      description="URL-friendly catrgory name")

class CategoryCreate(CategoryBase):
    pass

class CategotyResponse(CategoryBase):
    id: int = Field(..., description='Unique categoty indentifier')

    class Config:
        form_attributes = True
