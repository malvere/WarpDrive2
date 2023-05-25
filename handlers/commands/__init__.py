from aiogram import Dispatcher

from middleware.processor import ProcessorMiddleware

from .admin_tool import admin_tool
from .help import help
from .start import start
from .tools.admin_handler import admin, admin_only
from .wgcf_tool import wgcf_tool


def setup(dp: Dispatcher) -> None:
    """
    Commands setup

    :param dp: Corresponding Dispatcher
    """

    dp.register_message_handler(admin, admin_only, commands=["admin", "wgcf"])
    dp.register_message_handler(wgcf_tool, commands=["wgcf"])
    dp.register_message_handler(admin_tool, commands=["admin"])
    dp.middleware.setup(ProcessorMiddleware())
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
