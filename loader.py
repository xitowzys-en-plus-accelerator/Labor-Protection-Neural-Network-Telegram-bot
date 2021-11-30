import logging

from config import BOT_TOKEN
from handlers import pull_image_handler, run_test_handler

from telegram.ext import Updater, Filters, MessageHandler


def bootstrap() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.document & ~Filters.command, pull_image_handler))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, run_test_handler))

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater.start_polling()
    updater.idle()
