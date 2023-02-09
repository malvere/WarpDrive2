from asyncio import sleep

from aiogram.types import CallbackQuery

from warp.warp_basic import Config

from .. import keyboards as kb


async def config(call: CallbackQuery) -> None:
    """
    Callback handler for "config"

    :param call:
    """
    await call.message.edit_text("Обработка запроса")
    await sleep(0.5)
    conf = Config("warp.conf")
    await call.message.edit_text("Генерация конфига")
    await conf.get()
    await sleep(0.5)
    await call.message.edit_text("Отправляю")
    await sleep(0.5)
    with open("warp/cert/warp.conf", "rb") as f:
        await call.message.reply_document(f)
    await call.message.edit_text("Готово!", reply_markup=kb.generate_qrcode)
