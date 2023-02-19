# from asyncio import run, sleep

from aiogram.types import CallbackQuery, ParseMode
from aiogram.utils.markdown import text

from warp.warp_plus import WGCF

from .. import keyboards as kb


async def plus_config(call: CallbackQuery) -> None:
    """
    Callback handler for Warp+ configs
    Uses WGCF Class from warp_plus to generate corresponding config

    :param call:
    """
    await call.message.edit_text("Обработка запроса, процесс может занять до 2 минут")
    conf = WGCF("WarpPlus")
    try:
        await conf.get_license()
        conf.start()
        await call.message.edit_text("Конфигурация готова")
        with open("warp/cert/WarpPlus.conf", "rb") as f:
            await call.message.reply_document(f)
        await call.message.edit_text("Готово!", reply_markup=kb.generate_qrcode_plus)
    except Exception as ex:
        ex_message = f"Type: {type(ex).__name__}"
        ex_text = text(
            ("Ошибка генерации, слишком много запросов.\n"),
            ("Попробуйте через 10 минут.\n\n\n"),
            (f"Details: ||{ex_message}||"),
        )
        await call.message.edit_text(ex_text, parse_mode=ParseMode.MARKDOWN)
