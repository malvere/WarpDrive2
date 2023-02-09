# Модуль администрирования
from aiogram import types

from envars import ADMIN

admins = [int(ADMIN)]
admin_only = lambda msg: msg.from_user.id not in admins


async def admin(msg: types.Message) -> None:
    """
    Performs action in user is not admin

    :param msg:
    """
    await msg.delete()
