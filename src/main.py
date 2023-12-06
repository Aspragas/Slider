"""Image class with some attributes and main function."""
import tensorflow as tf
from materials import Image, Sound, Video

if __name__ == '__main__':

    print('TensorFlow version:', tf.__version__)

    image: Image = Image()
    image.read('resources/photos/cat.jpg')
    image.show('Deneme Kedi')

    video: Video = Video()
    video.read('resources/videos/dog.mp4')
    video.show('Deneme Kopek Video - ESC to Exit')
    video.release()

    last_frame: Image = video.get_last_frame()
    last_frame.show('Last frame')

    sound: Sound = Sound()
    sound.play('Hellooo')
    sound.play([1, 3, 5, 6, 4])
