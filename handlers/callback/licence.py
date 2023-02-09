from asyncio import run, sleep

from aiogram.types import CallbackQuery, ParseMode
from aiogram.utils.markdown import bold, text

from .. import keyboards as kb


async def license(call: CallbackQuery) -> None:
    """
    Callback handler for "license"

    Generates 12PB license key

    :param call:
    """
    await call.message.edit_text("Подготовка к генерации ключа...")
    await sleep(0.5)
    await call.message.edit_text("Генерация ключа")
    await sleep(0.5)
    await call.message.edit_text("Процесс займёт до 1 минуты")
    try:
        from warp import gen_warp

        # await call.message.edit_text(f"Попытка генерации ключа")
        key, limit = gen_warp.gen()
        if limit > 1000:
            license_message = text(
                bold("Ключ готов: \n"),
                (f"`{key}`\n"),
                ("Для копиравания нажми на ключ"),
                (f"Квота: {limit}"),
                sep="\n",
            )
            await call.message.edit_text(license_message, parse_mode=ParseMode.MARKDOWN)
        else:
            await call.message.edit_text(f"Квота: {limit}\nПерегенерировать?", reply_markup=kb.regen)

    except Exception as ex:
        ex_message = f"Type: {type(ex).__name__}"
        await call.message.edit_text(f"Ошибка генерации, попробуйте через 10 минут. \nDetails: {ex_message}\n{ex}")
