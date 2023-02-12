from aiogram import Dispatcher

from .config import config
from .generate_qr import generate_qr
from .licence import license
from .plus_config import plus_config
from .tools.member_handler import filtered_calls, member, member_status


def setup(dp: Dispatcher) -> None:
    """
    Callback setup

    :param dp: Corresponding Dispatcher
    """
    dp.register_callback_query_handler(member, member_status, lambda call: call.data in filtered_calls)
    dp.register_callback_query_handler(config, lambda call: call.data == "config")
    dp.register_callback_query_handler(plus_config, text="plus-config")
    dp.register_callback_query_handler(generate_qr, lambda call: call.data.startswith("generate-qr-code"))
    dp.register_callback_query_handler(license, text="licence")
