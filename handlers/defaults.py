from libs.libs import *
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    safe_name = html_escape(message.from_user.full_name)
    user_id = message.from_user.id
    link = f'<a href="tg://user?id={user_id}">{safe_name}</a>'
    await message.answer(f"Hello, {link}!", parse_mode="HTML")


@dp.message(lambda message: message.text.startswith("#savol"))
async def question_added(message: Message):
    await message.answer(f"{message.text} added!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")