from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "date" (
    "date" DATE NOT NULL  PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "cargotype" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(50) NOT NULL,
    "rate" DECIMAL(6,4) NOT NULL,
    "date_id" DATE NOT NULL REFERENCES "date" ("date") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
