import utils.imageProcessing as imageP
from config import ID_ADMIN

import os

from telegram import Update
from telegram.ext import CallbackContext


def pull_image_handler(update: Update, context: CallbackContext) -> None:
    path = "custom/test1.jpg"

    if not os.path.exists("./custom"):
        os.makedirs("./custom")

    with open(path, 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)

    image, msg = imageP.start(path)

    update.message.reply_text(
        text="Фото отправлено на проверку"
    )

    context.bot.send_photo(
        chat_id=ID_ADMIN,
        photo=image,
        caption=msg
    )
