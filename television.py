class Television:
    """
    Class representing values from a television
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to initialize the values needed for the tv.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the tv on and off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to mute and unmute the tv.
        """
        if self.__status:
            if self.__muted:
                self.__volume = Television.MIN_VOLUME
                self.__muted = False
            else:
                self.__volume = self.__volume
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__status:
            if self.__muted:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
            else:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            if self.__muted:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
            else:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
