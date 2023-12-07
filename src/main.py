"""Image class with some attributes and main function."""
import tensorflow as tf
from materials import Image, Sound, Video
from utils import Logger

if __name__ == '__main__':

    print('TensorFlow version:', tf.__version__)

    image: Image = Image()
    image.read('resources/photos/cat.jpg')
    image.show('Cat Picture')

    Logger.debug('image closed.')

    video: Video = Video()
    video.read('resources/videos/dog.mp4')
    video.show('Dog Video - ESC to Exit')
    video.release()

    Logger.critical('video released.')

    # TODO(Can Inal): Last frame will not be available
    # if we do not manually close the video window with ESC
    # https://github.com/Aspragas/Slider/issues/1
    last_frame: Image = video.get_last_frame()
    last_frame.show('Last frame')

    sound: Sound = Sound()
    sound.play('Hellooo')
    sound.play([1, 3, 5, 6, 4])

    Logger.error('Done.')
