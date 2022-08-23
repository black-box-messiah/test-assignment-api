from pydantic import BaseModel, Field

from .product import Product


class Stock(BaseModel):
    """Модель, представляющая данные о списке продуктов. Используется для валидации."""

    name: str
    list_: list[Product] = Field(..., alias='list')


class StockList(BaseModel):
    """Модель, представляющая данные о списке Stock (списков продуктов). Используется для валидации."""
    list_: list[Stock] = Field(..., alias='list')
