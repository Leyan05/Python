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
        self.__status = False  # TV is initially off
        self.__muted = False  # Mute is initially off
        self.__volume = Television.MIN_VOLUME  # Initial volume
        self.__channel = Television.MIN_CHANNEL  # Initial channel
    
    def power(self) -> None:
        """Toggle the power status of the television.
        :return: None"""
        self.__status = not self.__status
    
    def mute(self) -> None:
        """Toggle the mute status of the television if the power is on.
        :return: None"""
        if self.__status:
            self.__muted = not self.__muted
    
    def channel_up(self) -> None:
        """Increase the channel number by one, wrapping to the minimum channel if at the maximum.
        :return: None"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    
    def channel_down(self) -> None:
        """Decrease the channel number by one, wrapping to the maximum channel if at the minimum.
        :return: None"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self) -> None:
        """Increase the volume by one, up to the maximum volume, while also
        unmuting the TV if it was muted. :return: None"""
        if self.__status:
            self.__muted = False  # Unmute when volume is adjusted
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one, down to the minimum volume, while also
        unmuting the TV if it was muted. :return: None"""
        if self.__status:
            self.__muted = False  # Unmute when volume is adjusted
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the string representation of the television's current state. :return: str"""
        volume_display = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"