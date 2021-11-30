from typing import Any

import cv2 as cv
from PIL import Image
import numpy as np

from io import BytesIO


def numpy_to_binary(arr):
    arr = cv.cvtColor(arr, cv.COLOR_BGR2RGB)
    is_success, buffer = cv.imencode(".jpg", arr)
    io_buf = BytesIO(buffer)
    return io_buf.read()


def start(path) -> tuple[bytes, str]:
    """
    Handling the sent image by the user and sending it back to the user

    :param image: image in numpy array
    :return: binary image
    """
    img = Image.open(path)
    image = np.array(img)

    image_invert = np.invert(image)
    msg = "Нарушение"

    return numpy_to_binary(image_invert), msg


def test_start(test_number: int) -> tuple[Any, str, str]:
    msg = ""
    errors = ""

    if (test_number == 1):
        ...
        img = Image.open("custom/test1.jpg")
        image = np.array(img)

        # image_invert = np.invert(image)
        msg = "Тестовое изображение. Не нарушено :)"

        return numpy_to_binary(image), msg, errors
    else:
        errors = "Тест не найден"
        return None, msg, errors
