import environs
from aiogram import Bot, Dispatcher, html

env = environs.Env()
env.read_env("db/.env")
TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
dp = Dispatcher()
