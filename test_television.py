import pytest
from television import Television

def test_init():
    tv = Television()
    assert tv._status == False
    assert tv._muted == False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._status == True
    tv.power()
    assert tv._status == False

def test_mute():
    tv = Television()
    tv.mute()
    assert tv._muted == False  # Should do nothing when off
    tv.power()
    tv.mute()
    assert tv._muted == True
    tv.mute()
    assert tv._muted == False

def test_channel_up():
    tv = Television()
    tv.power()
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL

def test_channel_down():
    tv = Television()
    tv.power()
    tv._channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL

def test_volume_up():
    tv = Television()
    tv.power()
    tv._volume = Television.MAX_VOLUME
    tv._muted = True
    tv.volume_up()
    assert tv._muted == False
    assert tv._volume == Television.MAX_VOLUME

def test_volume_down():
    tv = Television()
    tv.power()
    tv._volume = Television.MIN_VOLUME
    tv._muted = True
    tv.volume_down()
    assert tv._muted == False
    assert tv._volume == Television.MIN_VOLUME

def test_str_method():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 1"
