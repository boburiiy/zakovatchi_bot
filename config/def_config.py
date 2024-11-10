import environs
from aiogram import Bot, Dispatcher
env = environs.Env()
dp = Dispatcher()

env.read_env("db/.env")
TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")


class db_config:
    DB_USER = env.str("DB_USER"),
    DB_PASSWD = env.str("DB_PASS"),
    DB_NAME = env.str("DB_NAME"),
    DB_HOST = env.str("DB_HOST"),
    DB_PORT = env.str("DB_PORT"),

    @classmethod
    def __str__(self) -> str:
        return [db_config.DB_NAME, db_config.DB_USER, db_config.DB_PASSWD, db_config.DB_HOST, db_config.DB_PORT]
