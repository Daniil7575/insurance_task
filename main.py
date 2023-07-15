from decimal import Decimal

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise.transactions import in_transaction

import models
import schemas
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from utils import add_tariff_to_db


app = FastAPI(title="Ensurance calculator")


# Посчитать стоимость
@app.post("/calculate-cost")
async def calculate_cost(cargo: schemas.Cargo):
    cargo_type = (
        await models.CargoType.filter(cargo_type=cargo.model_dump()["cargo_type"])
        .order_by("-date_id")
        .first()
    )

    # Если в базе данных есть тариф для данного типа груза, то используется наиболее актуальный
    # Иначе стоимость остается прежней
    cost = cargo.cost * cargo_type.rate if cargo_type else cargo.cost

    return {"status": 200, "data": {"cost": cost}}


# Загрузить json с API
@app.post("/add-rate")
async def add_rate(tariff: schemas.Tariff):
    data = tariff.model_dump()
    async with in_transaction():
        await add_tariff_to_db(data["json_"])
    return {"status": 200}


register_tortoise(
    app,
    db_url=f"asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    modules={"models": ["models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
