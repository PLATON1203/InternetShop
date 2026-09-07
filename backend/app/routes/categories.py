from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.category_service import CategotyService
from ..schemas.category import CategotyResponse

router = APIRouter(
    prefix='/api/categories',
    tags=['categories']
)
