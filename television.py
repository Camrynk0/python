class Television:
    """
    A class to simulate a basic television with power, channel, volume,
    and mute functionality.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes the Television object with default settings."""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggles the power status of the television."""
        self._status = not self._status

    def mute(self) -> None:
        """Toggles the mute status of the television when powered on."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        """Increases the channel by one, wrapping to minimum channel if at maximum."""
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """Decreases the channel by one, wrapping to maximum channel if at minimum."""
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        """Increases the volume by one, up to maximum, and unmutes if muted."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """Decreases the volume by one, down to minimum, and unmutes if muted."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        Returns the television's current state as a formatted string
        in the form 'Power = {status}, Channel = {channel}, Volume = {volume}'.
        """
        volume = 0 if self._muted and self._status else self._volume
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {volume}"
