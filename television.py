class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television with default settings.
        Initial settings:
        Power is off, volume is at minimum, channel is at minimum, and mute is off.
        """
        self.status = False  # TV is initially off
        self.muted = False  # Mute is initially off
        self.volume = Television.MIN_VOLUME  # Initial volume
        self.channel = Television.MIN_CHANNEL  # Initial channel
    
    def power(self):
        """Toggle the power status of the television."""
        self.status = not self.status
    
    def mute(self):
        """Toggle the mute status of the television if the power is on."""
        if self.status:
            self.muted = not self.muted
    
    def channel_up(self):
        """Increase the channel number by one, wrapping to the minimum channel if at the maximum."""
        if self.status:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL
    
    def channel_down(self):
        """Decrease the channel number by one, wrapping to the maximum channel if at the minimum."""
        if self.status:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL
    
    def volume_up(self):
        """Increase the volume by one, up to the maximum volume, while also
        unmuting the TV if it was muted.
        """
        if self.status:
            self.muted = False  # Unmute when volume is adjusted
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        """Decrease the volume by one, down to the minimum volume, while also
        unmuting the TV if it was muted.
        """
        if self.status:
            self.muted = False  # Unmute when volume is adjusted
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        """Return the string representation of the television's current state."""
        volume_display = 0 if self.muted else self.volume
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {volume_display}"