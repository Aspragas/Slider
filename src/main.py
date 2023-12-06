"""Image class with some attributes and main function."""
import tensorflow as tf
from materials import Image, Video

if __name__ == '__main__':

    print('TensorFlow version:', tf.__version__)

    img: Image = Image()
    img.read('resources/photos/cat.jpg')
    img.show('Deneme Kedi')

    video: Video = Video()
    video.read('resources/videos/dog.mp4')
    video.show('Deneme Kopek Video - ESC to Exit')
    video.release()
