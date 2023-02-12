from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""
Keyboards module
"""

startup = InlineKeyboardMarkup(row_width=2)
startup.insert(InlineKeyboardButton("Получить .conf", callback_data="config"))
startup.insert(InlineKeyboardButton("Сгенерировать ключ", callback_data="licence"))
startup.insert(InlineKeyboardButton("Получить WarpPlus.conf", callback_data="plus-config"))

join = InlineKeyboardMarkup()
join.insert(InlineKeyboardButton("Подписаться", url="https://t.me/+76CBN1H44BUwOWIy"))

regen = InlineKeyboardMarkup()
regen.insert(InlineKeyboardButton("Повторить", callback_data="licence"))

generate_qrcode = InlineKeyboardMarkup()
generate_qrcode.insert(InlineKeyboardButton(text="Сгенерировать QR-Код", callback_data="generate-qr-code\\basic"))

generate_qrcode_plus = InlineKeyboardMarkup()
generate_qrcode_plus.insert(InlineKeyboardButton(text="Сгенерировать QR-Код", callback_data="generate-qr-code\\plus"))
