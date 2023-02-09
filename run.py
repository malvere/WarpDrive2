# Imports
from imports import *

# Bot Init


# Logging
async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=env.API_TOKEN)
    dp = Dispatcher(bot)

    dp.middleware.setup(LoggingMiddleware())

    async def on_startup(self):
        logging.warning("Starting webhook..")
        await bot.delete_webhook()
        await bot.set_my_commands(commands=set_cmd())
        await bot.set_webhook(env.WEBHOOK_URL)
        commands.setup(dp)
        callback.setup(dp)

    async def on_shutdown(self):
        logging.warning("Shutting down..")
        logging.warning("Bye!")

    asyncio.run(
        start_webhook(
            dispatcher=dp,
            webhook_path=env.WEBHOOK_URL_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=False,
            host=env.WEBAPP_HOST,
            port=env.WEBAPP_PORT,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
