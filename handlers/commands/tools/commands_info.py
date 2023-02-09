from aiogram.types import BotCommand

commands_list = (
    ("start", "Начало работы", "Запустите команду, чтобы показать меню"),
    ("help", "Помощь по настройке", "Если у вас возникли проблемы с работой конфигов, пропишите /help"),
)


def set_cmd():
    """
    Sets a commands list with descriptions
    """
    bot_commands = []

    for cmd in commands_list:
        bot_commands.append(BotCommand(command=cmd[0], description=cmd[1]))
    return bot_commands
