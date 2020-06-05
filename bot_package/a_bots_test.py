import os
from bot_package.bot_commands import start
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()


def main():
    """main function to start bot work on local server"""

    updater = Updater(os.getenv("BOT_TOKEN"), use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)  # registering start handler in bot's dispatcher
    updater.start_polling()


if __name__ == '__main__':
    main()
