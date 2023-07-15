import json

from tortoise import Tortoise, run_async
from tortoise.transactions import in_transaction

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from utils import add_tariff_to_db


# Добавить тариф из json
async def add_tariff(
    tariff_json_path: str = "example.json", exec_untill_error: bool = False
) -> None:
    await Tortoise.init(
        db_url=f"asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        modules={"models": ["models"]},
    )
    # прочитать json и записать в tariff
    with open(tariff_json_path, "r") as j:
        tariff: dict = json.load(j)

    if exec_untill_error:
        # добавлять до первой ошибки
        await add_tariff_to_db(tariff)
    else:
        # добавить все или ничего
        async with in_transaction():
            await add_tariff_to_db(tariff)


if __name__ == "__main__":
    run_async(add_tariff())
