import allure
import requests
from entities.stock import StockList


class Stock:
    def __init__(self, session: requests.Session) -> None:
        self._session = session

    def get_stock_list(self) -> StockList:
        with allure.step("Выполнение запроса: GET https://apteka.magnit.ru/api/app/stock/list"):
            response = self._session.get("https://apteka.magnit.ru/api/app/stock/list")
            body = response.json()
        
        with allure.step("Валидация данных"):
            stock_list = StockList(**body)  # несоответствие схеме вызовет pydantic.ValidationError

        return stock_list
