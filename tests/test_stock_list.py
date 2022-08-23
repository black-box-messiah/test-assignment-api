import allure
import requests
from api.stock import Stock


@allure.feature("Список товаров")
class TestStockList:
    @allure.title("Получение списка товаров")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_schema_and_order(self, session: requests.Session):
        stock_list = Stock(session).get_stock_list()

        # проверить, отсортированы ли элементы нулевого Stock:
        with allure.step("Проверка сортировки товаров"):
            stock = stock_list.list_[0]
            sort_keys = [product.sort for product in stock.list_]
            assert sort_keys == sorted(sort_keys), "Элементы не отсортированы по полю \"sort\""
