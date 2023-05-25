# import asyncio

from aiogram.types import CallbackQuery, ParseMode
from aiogram.utils.markdown import bold, text

from .. import keyboards as kb


async def license(call: CallbackQuery) -> None:
    """
    Callback handler for "license"

    Generates 12PB license key

    :param call:
    """
    await call.message.edit_text("Процесс займёт до 1 минуты")
    try:
        from warp import async_wg

        warp = await async_wg.gen()
        if warp.check_limit():
            license_message = text(
                bold("Ключ готов: \n"),
                (f"`{warp.key}`\n"),
                ("Для копиравания нажми на ключ"),
                (f"Квота: {warp.limit}"),
                sep="\n",
            )
            await call.message.edit_text(license_message, parse_mode=ParseMode.MARKDOWN)
        else:
            await call.message.edit_text(f"Квота: {warp.limit}\nПерегенерировать?", reply_markup=kb.regen)

    except Exception as ex:
        ex_message = f"Type: {type(ex).__name__}"
        ex_text = text(
            ("Ошибка генерации, слишком много запросов на сервере. Повторите попытку через 10 минут."),
        )
        await call.message.edit_text(ex_text, parse_mode=ParseMode.MARKDOWN)
