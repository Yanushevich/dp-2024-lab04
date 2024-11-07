from datetime import datetime
from interfaces import BaseDigitalClock, BaseAnalogClock
from clocks.time_converter import TimeConverter


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
        self._date = datetime.today()

    def set_date_time(self, date: datetime) -> None:
        """
        Устанавливает дату, сохраняя данные в аналоговом формате

        :param date: дата в формате datetime
        """
        self._date = date
        self._analog_clock.set_date_time(
            self._date.year,
            self._date.month,
            self._date.day,
            TimeConverter.get_hour_angle(self._date.hour, self._date.minute),
            TimeConverter.get_minute_angle(self._date.minute, self._date.second),
            TimeConverter.get_second_angle(self._date.second),
            TimeConverter.get_day_night_division(self._date.hour),
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
            TimeConverter.get_hour(self._analog_clock.get_hour_angle(), self._analog_clock.get_day_night_division()),
            TimeConverter.get_minute(self._analog_clock.get_minute_angle()),
            TimeConverter.get_second(self._analog_clock.get_second_angle())
        )
