"""Video Class."""
import cv2 as cv


class Video:
    """Video class."""

    def __init__(self) -> None:
        """Initialization of Video class."""
        self._capture: cv.VideoCapture = cv.VideoCapture()

    def read(self, video: str | int) -> None:
        """Reading video."""
        self._capture = cv.VideoCapture(video)

    def show(self, window_title: str) -> None:
        """Showing video."""
        while self._capture.read()[0]:
            frame = self._capture.read()[1]
            cv.imshow(window_title, frame)

            if cv.waitKey(20) and ord('d') == 0xFF:
                break

    def release(self) -> None:
        """Releasing video."""
        self._capture.release()
        cv.destroyAllWindows()
