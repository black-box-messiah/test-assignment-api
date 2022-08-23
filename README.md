## Тестовое задание (API)

### Установка и запуск

Необходим Python версии не ниже 3.10

#### Установка
```
pip install -r requirements.txt
```

#### Запуск
```
python -m pytest
```

### Условие
Реализовать тест для проверки метода API по следующему кейсу:

1. Отправить запрос `GET https://apteka.magnit.ru/api/app/stock/list`
 
Ожидаемое поведение: 
- Элементы в массиве поля `list` отсортированы по значению указанному в поле `sort` для каждого элемента.
- JSON схема валидна (принять текущую схему ответа за истину).