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
        while True:
            ret, frame = self._capture.read()

            if not ret:
                # Break the loop if no more frames are available
                break

            cv.imshow(window_title, frame)

            # Check for the 'ESC' key (27 is the ASCII code for ESC)
            key = cv.waitKey(20) & 0xFF
            if key == 27:
                break

    def release(self) -> None:
        """Releasing video."""
        self._capture.release()
        cv.destroyAllWindows()
