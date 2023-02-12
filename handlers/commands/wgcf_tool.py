from aiogram import types

from warp.warp_plus import WGCF

from .. import keyboards as kb


async def wgcf_tool(msg: types.Message) -> None:
    """
    WGCF Handler

    Allows for .conf generation with existing CloudFlare Warp key

    :param call:
    """
    args = msg.get_args()
    if args:
        conf = WGCF(filename="WarpPlus", licence=args)
        try:
            await conf.get_license()
            conf.start()
            with open("warp/cert/WarpPlus.conf", "rb") as f:
                await msg.reply_document(f, reply_markup=kb.generate_qrcode_plus)
        except Exception as ex:
            ex_message = f"Type: {type(ex).__name__}"
        await msg.answer(f"Ошибка генерации, попробуйте через 10 минут. \nDetails: {ex_message}\n{ex}")
    else:
        await msg.answer("No args")
