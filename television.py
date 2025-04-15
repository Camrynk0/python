class Television:
    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Private instance variables
        self._status = False  # TV is off
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def mute(self):
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self):
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        display_volume = 0 if self._muted and self._status else self._volume
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {display_volume}"
