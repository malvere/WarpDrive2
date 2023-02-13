from aiogram import types

from .. import keyboards as kb


async def start(msg: types.Message) -> None:
    """
    Command handler for /start
    Drops Bot's main menu

    :param msg:
    """
    await msg.answer("Добро пожаловать! \nВыберите что вам нужно:", reply_markup=kb.startup)
