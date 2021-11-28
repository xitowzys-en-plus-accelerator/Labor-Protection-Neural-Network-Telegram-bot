import utils.imageProcessing as imageP
from config import ID_ADMIN

from skimage import io

from telegram import Update
from telegram.ext import CallbackContext


def pull_image_handler(update: Update, context: CallbackContext) -> None:
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.getFile(file_id)

    image = io.imread(newFile['file_path'])

    image, msg = imageP.start(image)

    update.message.reply_text(
        text="Фото отправлено на проверку"
    )

    context.bot.send_photo(
        chat_id=ID_ADMIN,
        photo=image,
        caption=msg
    )
