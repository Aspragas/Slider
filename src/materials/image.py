"""Image Class."""
import cv2 as cv
import numpy as np


class Image:
    """Image class."""

    def __init__(self, image_array: list[int] | None = None) -> None:
        """Initializes Image class. If an image_array is not given then we should read
        from a file using read() function.

        Args:
            image_array (list[int] | None, optional): To create an image with given image array.
            Defaults to None.
        """  # noqa: D205
        self._image_matrix: np.typing.NDArray[np.int64] = np.array(image_array, ndmin=3)

    def __repr__(self) -> str:
        """Str class override."""
        return f'Shape is {self.shape}.\nData is {self._image_matrix}'

    def read(self, image: str) -> None:
        """Reading image."""
        self._image_matrix = cv.imread(image)

    def show(self, window_title: str) -> None:
        """Show image."""
        cv.imshow(window_title, self._image_matrix)
        cv.waitKey(0)

    @property
    def shape(self) -> tuple[int, ...]:
        """Gets shape of image."""
        return self._image_matrix.shape
