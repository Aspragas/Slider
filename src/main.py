"""Entry point of application with main function."""
import os

from api import Recognizer
from materials import Image
from utils import Logger

# To hide warnings from tensorflow. Because we are using CPU not GPU.
# FIX IT!
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == '__main__':

    Logger.info('Logger started.')

    image: Image = Image()
    image.read('resources/photos/ocr.jpg')
    image.show('Test Data')

    print(image.image_array)

    recognizer: Recognizer = Recognizer()
    results = recognizer.recognize(image)
    print(results)
