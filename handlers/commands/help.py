from aiogram import types
from aiogram.utils.markdown import text

from .tools import commands_list as cmd_list


async def help(msg: types.Message) -> None:
    """
    Command handler for /start
    Used to get detailed help for Bot CMDs

    :param msg:
    """
    args = msg.get_args()
    if args:
        if args == cmd_list[0][0]:
            await msg.answer(f"{cmd_list[0][2]}")
        elif args == cmd_list[1][0]:
            await msg.answer(f"{cmd_list[1][2]}")
    else:
        await msg.answer(
            text(
                ("Установка профиля в WireGuard:"),
                ("\n"),
                ("- Нажмите на иконку 'отправить'"),
                ("- Выберить в появившемся меню 'WireGuard'\n"),
                ("Или:"),
                ("Сгенерируйте QR-Код после получения конфига"),
                ("Откройте WireGuard, Нажмите '+'"),
                ("Наведите камеру на QR-код (Например с ПК)"),
                sep="\n",
            )
        )
