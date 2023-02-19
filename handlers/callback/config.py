# from asyncio import sleep

from aiogram.types import CallbackQuery

from warp.warp_basic import Config

from .. import keyboards as kb


async def config(call: CallbackQuery) -> None:
    """
    Callback handler for "config"
    Outputs baisc config
    Currently available for non-member users, nehavior could be changed by adding callBackData to coresponding envar

    :param call:
    """
    await call.message.edit_text("Обработка запроса")
    conf = Config("warp.conf")
    await call.message.edit_text("Генерация конфига")
    await conf.get()
    await call.message.edit_text("Отправляю")
    with open("warp/cert/warp.conf", "rb") as f:
        await call.message.reply_document(f)
    await call.message.edit_text("Готово!", reply_markup=kb.generate_qrcode)
