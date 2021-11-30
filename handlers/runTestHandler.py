from telegram import Update
from telegram.ext import CallbackContext
import utils.imageProcessing as imageP


def run_test_handler(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text.isdigit():

        image, msg, err = imageP.test_start(int(text))

        if err:
            update.message.reply_text(
                text=err
            )
        else:
            update.message.reply_photo(
                photo=image,
                caption=msg
            )
    else:
        text = "Должен быть номер теста"

        update.message.reply_text(
            text=text
        )
