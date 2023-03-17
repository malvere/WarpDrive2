from aiogram.types import CallbackQuery

from warp.basic import WGCFBasic

from .. import keyboards as kb


async def config(call: CallbackQuery) -> None:
    """
    Callback handler for "config"
    Outputs baisc config
    Currently available for non-member users, behavior could be changed by adding callBackData to coresponding envar

    :param call:
    """
    await call.message.edit_text("Обработка запроса")
    conf = WGCFBasic("warp")
    await call.message.edit_text("Генерация конфига")
    try:
        conf.start()
        await call.message.edit_text("Отправляю")
        with open("warp/cert/warp.conf", "rb") as f:
            await call.message.reply_document(f)
        await call.message.edit_text("Готово!", reply_markup=kb.generate_qrcode)
    except Exception as ex:
        print(ex)
        pass
