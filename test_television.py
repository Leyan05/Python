import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def test_initial_state(self):
        assert not self.tv.__status
        assert self.tv.__volume == Television.MIN_VOLUME
        assert self.tv.__channel == Television.MIN_CHANNEL
        assert not self.tv.__muted
    
    def test_power_toggle(self):
        self.tv.power()
        assert self.tv.__status
        self.tv.power()
        assert not self.tv.__status
    
    def test_channel_up_wraps(self):
        self.tv.power()
        for _ in range(Television.MAX_CHANNEL):
            self.tv.channel_up()
        assert self.tv.__channel == Television.MAX_CHANNEL
        self.tv.channel_up()
        assert self.tv.__channel == Television.MIN_CHANNEL
    
    def test_channel_down_wraps(self):
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__channel == Television.MAX_CHANNEL
        for _ in range(Television.MAX_CHANNEL):
            self.tv.channel_down()
        assert self.tv.__channel == Television.MIN_CHANNEL
    
    
    def test_volume_up_limits(self):
        self.tv.power()
        for _ in range(Television.MAX_VOLUME):
            self.tv.volume_up()
        assert self.tv.__volume == Television.MAX_VOLUME
        self.tv.volume_up()
        assert self.tv.__volume == Television.MAX_VOLUME
    
    def test_volume_down_limits(self):
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__volume == Television.MIN_VOLUME
        self.tv.volume_up()  # Increase volume to avoid hitting min
        self.tv.volume_down()
        assert self.tv.__volume == Television.MIN_VOLUME
    
    def test_no_effect_when_off(self):
        self.tv.channel_up()
        assert self.tv.__channel == Television.MIN_CHANNEL
        self.tv.channel_down()
        assert self.tv.__channel == Television.MIN_CHANNEL
        self.tv.volume_up()
        assert self.tv.__volume == Television.MIN_VOLUME
        self.tv.volume_down()
        assert self.tv.__volume == Television.MIN_VOLUME
        self.tv.mute()
        assert not self.tv.__muted
    
    def test_mute_toggle(self):
        self.tv.power()
        self.tv.mute()
        assert self.tv.__muted
        self.tv.mute()
        assert not self.tv.__muted 
    
    def test_string_representation(self):
        self.tv.power()
        self.tv.channel_up()
        self.tv.volume_up()
        self.tv.mute()
        state_str = str(self.tv)
        assert "Power: On" in state_str
        assert f"Channel: {self.tv.__channel}" in state_str
        assert f"Volume: {self.tv.__volume}" in state_str
        assert "Muted: Yes" in state_str
    
    def test_string_representation_when_off(self):
        state_str = str(self.tv)
        assert "Power: Off" in state_str
        assert f"Channel: {self.tv.__channel}" in state_str
        assert f"Volume: {self.tv.__volume}" in state_str
        assert "Muted: No" in state_str
    