from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    """Модель, представляющая данные об одном продукте. Используется для валидации."""

    id: int
    title: Optional[str]
    title_color: Optional[str] = Field(..., alias='title-color')
    description: Optional[str]
    type: dict[str, str]
    image: str
    image_big: str = Field(..., alias="image-big")
    image_wide: str = Field(..., alias="image-wide")
    sort: int
    date_start: datetime = Field(..., alias="date-start")
    date_end: datetime = Field(..., alias="date-end")
    markers: list[Any]
