from datetime import datetime
from interfaces import BaseDigitalClock, BaseAnalogClock
from consts import DayNightDivision


class DigitalClockAdapter(BaseDigitalClock):
    """
    Адаптер для работы с интерфейсом цифровых часов
    """
    def __init__(self, analog_clock: BaseAnalogClock):
        """
        Инициализирует адаптер

        :param analog_clock: объект интерфейса аналоговых часов
        """
        self._analog_clock = analog_clock
        self.date = None

    def get_hour_angle(self) -> int:
        """
        Возвращает значение угла часовой стрелки, учитывая время в минутах

        :return: возвращает угол положения часовой стрелки в формате int
        """
        return 30 * (self.date.hour % 12) + self.date.minute * 0.5

    def get_hour(self) -> int:
        """
        Возвращает значение часа

        :return: возвращает значение времени в часах в формате int
        """
        return (
            int(self._analog_clock.get_hour_angle() // 30)
            if (self.get_day_night_division() == DayNightDivision.AM)
            else (int(self._analog_clock.get_hour_angle() // 30) + 12)
        )

    def get_minute_angle(self) -> int:
        """
        Возвращает значение угла минутной стрелки, учитывая время в секундах

        :return: возвращает угол положения минутной стрелки в формате int
        """
        return 6 * self.date.minute + self.date.second * 0.1

    def get_minute(self) -> int:
        """
        Возвращает значение минуты

        :return: возвращает значение времени в минутах в формате int
        """
        return int(self._analog_clock.get_minute_angle() // 6)

    def get_second_angle(self) -> int:
        """
        Возвращает значение угла секундной стрелки

        :return: возвращает угол положения секундной стрелки в формате int
        """
        return 6 * self.date.second

    def get_second(self) -> int:
        """
        Возвращает значение секунды

        :return: возвращает значение времени в секундах в формате int
        """
        return int(self._analog_clock.get_second_angle() // 6)

    def get_day_night_division(self):
        """
        Возвращает время суток

        :return: возвращает время суток в формате DayNightDivision
        """
        if self.date.hour > 11:
            return DayNightDivision.PM
        else:
            return DayNightDivision.AM

    def set_date_time(self, date: datetime) -> None:
        """
        Устанавливает дату, сохраняя данные в аналоговом формате

        :param date: дата в формате datetime
        """
        self.date = date
        self._analog_clock.set_date_time(
            self.date.year,
            self.date.month,
            self.date.day,
            self.get_hour_angle(),
            self.get_minute_angle(),
            self.get_second_angle(),
            self.get_day_night_division(),
        )

    def get_date_time(self) -> datetime:
        """
        Получает дату, обращаясь к объекту, хранящему данные в аналоговом формате

        :return: возвращает дату в формате datetime
        """
        return datetime(
            self._analog_clock.get_year(),
            self._analog_clock.get_month(),
            self._analog_clock.get_day(),
            self.get_hour(),
            self.get_minute(),
            self.get_second(),
        )
