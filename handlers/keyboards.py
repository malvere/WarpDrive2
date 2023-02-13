from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from envars import CHANNEL_URL

"""
Keyboards module
"""
# Reply Markup for /start
startup = InlineKeyboardMarkup(row_width=2)
startup.insert(InlineKeyboardButton("Получить .conf", callback_data="config"))
startup.insert(InlineKeyboardButton("Сгенерировать ключ", callback_data="licence"))
startup.insert(InlineKeyboardButton("Получить WarpPlus.conf", callback_data="plus-config"))

# Reply Markup for non-member users
join = InlineKeyboardMarkup()
join.insert(InlineKeyboardButton("Подписаться", url=CHANNEL_URL))

# Reply Markup for failed key-generation
regen = InlineKeyboardMarkup()
regen.insert(InlineKeyboardButton("Повторить", callback_data="licence"))

# Reply Markup for generating BasicConfig QR-Code
generate_qrcode = InlineKeyboardMarkup()
generate_qrcode.insert(InlineKeyboardButton(text="Сгенерировать QR-Код", callback_data="generate-qr-code\\basic"))

# Reply Markup for generating PlusConfig QR-Code
generate_qrcode_plus = InlineKeyboardMarkup()
generate_qrcode_plus.insert(InlineKeyboardButton(text="Сгенерировать QR-Код", callback_data="generate-qr-code\\plus"))
