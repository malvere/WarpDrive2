import platform
import socket

from aiogram import types


async def admin_tool(msg: types.Message) -> None:
    """
    Command handler for /admin

    Handles admin priveleges (test purposes)

    :param msg:
    """
    socket = socket.gethostname()
    system = platform.platform()
    await msg.answer(f"{system} \nSocket: {socket}")
