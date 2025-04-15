class Television:
    """
    A class to simulate a basic television with power, channel, volume,
    and mute functionality.
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initialize the Television with default settings:
        off, unmuted, min volume, and min channel.
        """
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """Toggle the power status of the television."""
        self._status = not self._status

    def mute(self):
        """
        Toggle the mute status of the television,
        only if the power is on.
        """
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """
        Increment the channel by 1, wrapping around
        to MIN_CHANNEL if at MAX_CHANNEL.
        Only works if the TV is on.
        """
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self):
        """
        Decrement the channel by 1, wrapping around
        to MAX_CHANNEL if at MIN_CHANNEL.
        Only works if the TV is on.
        """
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        """
        Increase the volume by 1, up to MAX_VOLUME.
        Automatically unmutes the TV if muted.
        Only works if the TV is on.
        """
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """
        Decrease the volume by 1, down to MIN_VOLUME.
        Automatically unmutes the TV if muted.
        Only works if the TV is on.
        """
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """
        Return a string representation of the TV's current state.
        If muted and powered on, volume is displayed as 0.
        """
        display_volume = 0 if self._muted and self._status else self._volume
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {display_volume}"
