from aiogram import types

from envars import CALL_FILTERS, CHANNEL_ID

from ... import keyboards as kb

filtered_calls = [
    "licence",
    "generate-qr-code\\basic",
    "generate-qr-code\\plus",
    "plus-config",
] + CALL_FILTERS


async def member_status(call: types.CallbackQuery):
    """
    Member status filter

    Returns True if user in not in chat

    :param call:
    """
    status = await call.bot.get_chat_member(CHANNEL_ID, call.from_user.id)
    return status.status == "left"


async def member(call: types.CallbackQuery):
    """
    Callback handler for non-subscribers

    :param call:
    """
    await call.message.edit_text(
        "Тебя нет в канале, чтобы пользоваться ботом подпишись по брацки", reply_markup=kb.join
    )
