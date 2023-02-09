from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""
Keyboards module
"""

startup = InlineKeyboardMarkup()
startup.insert(InlineKeyboardButton("Получить .conf", callback_data="config"))
startup.insert(InlineKeyboardButton("Сгенерировать ключ", callback_data="licence"))

join = InlineKeyboardMarkup()
join.insert(InlineKeyboardButton("Подписаться", url="https://t.me/+76CBN1H44BUwOWIy"))

regen = InlineKeyboardMarkup()
regen.insert(InlineKeyboardButton("Повторить", callback_data="licence"))

generate_qrcode = InlineKeyboardMarkup()
generate_qrcode.insert(InlineKeyboardButton(text="Сгенерировать QR-Код", callback_data="generate-qr-code"))
