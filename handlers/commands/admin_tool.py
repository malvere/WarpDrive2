import platform
from socket import gethostname

from aiogram import types


async def admin_tool(msg: types.Message) -> None:
    """
    Command handler for /admin

    Handles admin priveleges (test purposes)

    :param msg:
    """
    socket = gethostname()
    system = platform.platform()
    await msg.answer(f"{system} \nSocket: {socket}")
