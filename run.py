# Imports
from imports import *

# Bot Init

# Logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=env.API_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())


async def on_startup():
    logging.warning("Starting webhook..")
    await bot.delete_webhook()
    await bot.set_my_commands(commands=set_cmd())
    await bot.set_webhook(env.WEBHOOK_URL, drop_pending_updates=False)


async def on_shutdown():
    logging.warning("Shutting down..")
    logging.warning("Bye!")


if __name__ == "__main__":
    commands.setup(dp)
    callback.setup(dp)
    start_webhook(
        dispatcher=dp,
        webhook_path=env.WEBHOOK_URL_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=False,
        host=env.WEBAPP_HOST,
        port=env.WEBAPP_PORT,
    )
