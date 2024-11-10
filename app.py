from libs.libs import *


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    for admin in ADMINS:
        await bot.send_message(admin, 'bot ishga tushdi')
    await dp.start_polling(bot)


if __name__ == "__main__":
    os.system("clear || cls")
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("good bye :)")