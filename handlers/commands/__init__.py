from aiogram import Dispatcher

from .admin_tool import admin_tool
from .help import help
from .start import start
from .tools.admin_handler import admin, admin_only


def setup(dp: Dispatcher) -> None:
    """
    Commands setup

    :param dp: Corresponding Dispatcher
    """
    dp.register_message_handler(admin, admin_only, commands=["admin"])
    dp.register_message_handler(admin_tool, commands=["admin"])
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
