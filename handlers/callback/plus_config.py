# from asyncio import run, sleep

from aiogram.types import CallbackQuery

from warp.warp_plus import WGCF

from .. import keyboards as kb


async def plus_config(call: CallbackQuery) -> None:
    """
    Callback handler for Warp+ configs
    Uses WGCF Class from warp_plus to generate corresponding config

    :param call:
    """
    await call.message.edit_text("Обработка запроса, процесс может занять до 2 минут")
    # await sleep(1)

    conf = WGCF("WarpPlus")
    try:
        await conf.get_license()
        conf.start()
        await call.message.edit_text("Конфигурация готова")
        # await sleep(1)
        with open("warp/cert/WarpPlus.conf", "rb") as f:
            await call.message.reply_document(f)
        await call.message.edit_text("Готово!", reply_markup=kb.generate_qrcode_plus)
    except Exception as ex:
        ex_message = f"Type: {type(ex).__name__}"
        await call.message.edit_text(f"Ошибка генерации, попробуйте через 10 минут. \nDetails: {ex_message}\n{ex}")
