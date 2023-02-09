from asyncio import sleep

import qrcode
from aiogram.types import CallbackQuery


async def generate_qr(call: CallbackQuery) -> None:
    """
    Callback handler for "generate-qr-code"

    Generates QR code for WireGuard Config

    :param call:
    """
    conf_path = "warp/cert/warp.conf"
    qr_path = "warp/cert/qr_basic.png"
    await call.message.edit_text("Генерирую QR-Код")
    await sleep(0.5)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_M,
    )
    with open(conf_path, "r") as conf:
        data = conf.read()
        qr.add_data(data)

    img = qr.make_image(fill_color="white", back_color="black")
    img.save(qr_path)

    with open(qr_path, "rb") as png:
        await call.message.answer_photo(photo=png)
        await call.message.delete()
