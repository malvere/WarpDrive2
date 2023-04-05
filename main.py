# Imports
from imports import *


# Main function
def main() -> None:
    """
    Bots "Heart"

    Used to setup core-functionality
    """
    logging.basicConfig(level=logging.INFO)  # Logging

    bot = Bot(token=env.API_TOKEN)
    dp = Dispatcher(bot)

    dp.middleware.setup(LoggingMiddleware())  # Middleware setup

    async def on_startup(self):
        """
        Actions to perform on WebHook Startup:
        """
        logging.warning("Starting webhook..")
        await bot.delete_webhook()
        await bot.set_my_commands(commands=set_cmd())

        # Getting webhook info
        webhook = await bot.get_webhook_info()

        # Resolve webhook if BadUrl
        if webhook.url != env.WEBHOOK_URL:
            logging.warning(f"Bad webhook url: {webhook.url}, resolving...")
            if not webhook.url:
                await bot.delete_webhook()
                logging.warning("Webhook url deleted")
            await bot.set_webhook(env.WEBHOOK_URL)
        commands.setup(dp)  # Setup CMDs
        callback.setup(dp)  # Setup callback

    async def on_shutdown(self):
        """
        Actions to perform on WebHook Shutdown

        Note: self.delete_webhook() is not used due to startrup issues
        When running on hosting
        """
        logging.warning("Shutting down..")
        logging.warning("Bye!")

    start_webhook(
        dispatcher=dp,
        webhook_path=env.WEBHOOK_URL_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=env.WEBAPP_HOST,
        port=env.WEBAPP_PORT,
    )


if __name__ == "__main__":
    main()
