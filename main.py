from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
import logging

import commands
from utils import current_time


def main():

    load_dotenv('/home/ilkka/Python/telegram_example/telegram.env')

    updater = Updater(token=os.getenv('TOKEN'), use_context=True)
    dispatcher = updater.dispatcher

    for name, item in commands.__dict__.items():
        if callable(item) and item.__module__ == 'commands':
            dispatcher.add_handler(CommandHandler(name, item))

    # This should be last, so it responds only if the other handlers didn't.
    dispatcher.add_handler(MessageHandler(Filters.command, commands.unknown))

    updater.start_polling()


if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger(__name__)

    try:
        main()
    except Exception:
        logger.exception(current_time())
