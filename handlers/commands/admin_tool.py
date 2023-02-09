import platform

from aiogram import types


async def admin_tool(msg: types.Message) -> None:
    """
    Command handler for /admin

    Handles admin priveleges (test purposes)

    :param msg:
    """
    system = platform.platform()
    await msg.answer(f"System: {system}")
