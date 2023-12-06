"""Sound class."""
from functools import singledispatchmethod

import pyaudio as audio


class Sound:
    """Sound class."""

    def __init__(self) -> None:
        """Initialization of Sound class."""
        self._audio: audio.PyAudio = audio.PyAudio()

    def record(self) -> None:
        """Starts recording audio."""

    @singledispatchmethod
    def play(self, sound: str | list | None = None) -> None:  # type: ignore  # noqa: PGH003
        """Plays a sound file or given sound array.

        Args:
            sound (str | int | None, optional): It is either sound file path or sound byte array.
            Defaults to None.
        """
        print('This function is not overloaded for ', type(sound), ' type.')

    @play.register
    def _(self, sound: str) -> None:
        """Overloaded version of base play().

        Args:
            sound (str): _description_
        """
        print('Hello Sound Str = ', sound)

    @play.register
    def _(self, sound: list) -> None:  # type: ignore  # noqa: PGH003
        """Overloaded version of base play().

        Args:
            sound (int): _description_
        """
        print('Hello Sound Int = ', sound)

    def stop(self) -> None:
        """Stops recording audio."""
