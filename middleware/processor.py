from asyncio import sleep
from typing import Union

from aiogram import Dispatcher
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import Throttled
from sqlalchemy import ScalarResult, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker as sessionmaker

from db import User, get_session_maker
from db.session import async_engine


class ProcessorMiddleware(BaseMiddleware):

    """
    Antiflood middleware
    """

    def __init__(self, limit=1.0, key_prefix="antiflood_"):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ProcessorMiddleware, self).__init__()

    async def process(self, event: Union[Message, CallbackQuery]):
        # Get current handler
        handler = current_handler.get()

        # Get dispatcher from context
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"

        try:
            await dispatcher.throttle(key, rate=limit)
            session_maker = get_session_maker(async_engine)
            ses = session_maker()
            async with ses as session:
                session: AsyncSession
                result = await session.execute(select(User).where(User.user_id == event.from_user.id))
                user: User = result.one_or_none()
                if isinstance(event, Message):
                    interaction = event.text
                else:
                    interaction = event.data.split(":")
                    interaction = interaction[0]
                if user is not None:
                    # Update existing user
                    stmt = (
                        update(User)
                        .where(User.user_id == event.from_user.id)
                        .values(
                            interaction=interaction,
                        )
                    )
                    await session.execute(stmt)
                    pass
                else:
                    # New User
                    user = User(
                        user_id=event.from_user.id,
                        username=event.from_user.username,
                        interaction=interaction,
                    )
                    await session.merge(user)
                    print("added user")
                await session.commit()

        except Throttled as t:
            if isinstance(event, Message):
                await self.message_throttled(event, t)
            else:
                await self.message_throttled(event.message, t)

            # Cancell Next Handler
            raise CancelHandler()

    async def on_process_message(self, message: Message, data: dict):
        """
        This handler is called when dispatcher receives a message

          :param message:
        """
        await self.process(message)

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        """
        This handler is called when dispatcher receives a callback

          :param call:
        """
        await self.process(call)

    async def message_throttled(self, message: Message, throttled: Throttled):
        """
        Notify user only on first exceed and notify about unlocking only on last exceed

        :param message:
        :param throttled:
        """
        handler = current_handler.get()
        # dispatcher = Dispatcher.get_current()
        if handler:
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            key = f"{self.prefix}_message"

        # Calculate how many time is left till the block ends
        delta = throttled.rate - throttled.delta

        # Prevent flooding
        if throttled.exceeded_count <= 2:
            await message.answer("Подождите перед следующим запросом.")

        # Sleep.
        await sleep(delta)

        # Check lock status
        # thr = await dispatcher.check_key(key)

        # # If current message is not last with current key - do not send message
        # if thr.exceeded_count == throttled.exceeded_count:
        #     await message.answer("Флуд-блок снят")
