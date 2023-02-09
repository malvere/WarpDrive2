from typing import Any, Awaitable, Callable, Dict

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        return handler(event, data)
