from typing import Dict, List

import models


# Добавить в бд
async def add_tariff_to_db(tariff: Dict[str, List[Dict]]) -> None:
    # перебор тарифов по датам
    for date_, options in tariff.items():
        # добавление даты в бд
        date_obj = await models.Date.create(date=date_)
        # перебор списка категорий тарифов
        for option in options:
            await models.CargoType.create(**option, date=date_obj)
