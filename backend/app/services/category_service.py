from sqlalchemy.orm import Session
from typing import List
from ..repositories.categoty_repository import CategoryRepository
from ..schemas.category import CategotyResponse, CategoryCreate
from fastapi import HTTPException, status