"""Recognizer class."""
import keras_ocr  # type: ignore  # noqa: PGH003
from materials import Image


class Recognizer:
    """Recognizer class."""

    def __init__(self) -> None:
        """Initialization of Recognizer class."""
        self._pipeline: keras_ocr.pipeline.Pipeline = keras_ocr.pipeline.Pipeline()

    def recognize(self, image: Image) -> list[str]:
        """Recognizes text from a given image.

        Args:
            image (Image): _description_

        Returns:
            list[list[tuple[str, list[tuple[npt.NDArray[np.int64], str]] | tuple[str, npt.NDArray[np.int64]]]]]:
            _description_
        """  # noqa: E501
        image_ocr = [keras_ocr.tools.read(image.image_array)]
        results = self._pipeline.recognize(image_ocr)
        words: list[str] = [
            word for result in results for item in result for word in item if isinstance(word, str)
        ]
        return words
