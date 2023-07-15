# REST API сервис по расчёту стоимости страхования

## Развертывание

1) Склонируйте в удобную директорию репозиторий следующей командой: 
```
git clone https://github.com/Daniil7575/insurance_task.git
``` 
2) Перейдите в директорию ***insurance_task***.

3) ~~Создайте в склонированном репоизитории файл _**.env**_~~ Файл .env уже создан и заполнен (По хорошему он должен содержать только названия переменных без значений, но чтобы не тратить время значения были проставлены).

4) Соберите и запустите сервисы:
```
sudo docker compose build
sudo docker compose up
```
5) Дождитесь примерно такой записи лога:
```
insurance_task-web-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
6) Зайдите в документацию сервиса по адресу - http://0.0.0.0:8000/docs


## Структура
 
***config.py*** - Конфигурационный файл сервиса

***main.py*** - REST API сервис с двумя эндпоинтами: 
1) ```POST /calculate-cost``` - посчитать цену данного груза
2) ```POST /add-rate``` - добавить в бд новый тариф

***models.py*** - Модели базы данных

***schemas.py*** - Pydantic модели

***scripts.py*** - Скрипт для взаимодействия с сервисом 

***utils.py*** - Функция для добавления в базу данных тарифа

***migrations/*** - Директория с миграциями базы данных

***example.json*** - Пример принимаемого json документа (также используется как демонстарция работы скрипта из ***scripts.py***)