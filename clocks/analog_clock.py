from interfaces import BaseAnalogClock
from consts import DayNightDivision


class AnalogClock(BaseAnalogClock):
    """
    Класс для работы с аналоговыми часами
    """
    def __init__(self):
        """
        Инициализирует объект аналоговых часов
        """
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour_angle = 0.0
        self.minute_angle = 0.0
        self.second_angle = 0.0
        self.day_night_division = DayNightDivision.AM

    def set_date_time(
        self,
        year: int,
        month: int,
        day: int,
        hour_angle: float,
        minute_angle: float,
        second_angle: float,
        day_night_division: DayNightDivision,
    ):
        """
        Устанавливает дату

        :param year: год
        :param month: месяц
        :param day: день
        :param hour_angle: угол часовой стрелки
        :param minute_angle: угол минутной стрелки
        :param second_angle: угол секундной стрекли
        :param day_night_division: время суток (до полудня/после полудня)
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle
        self.second_angle = second_angle
        self.day_night_division = day_night_division

    def get_hour_angle(self) -> float:
        """
        Возвращает угол часовой стрелки

        :return: возвращает угол положения часовой стрелки в формате float
        """
        return self.hour_angle

    def get_minute_angle(self) -> float:
        """
        Возвращает угол минутной стрелки

        :return: возвращает угол положения минутной стрелки в формате float
        """
        return self.minute_angle

    def get_second_angle(self) -> float:
        """
        Возвращает угол секундной стрелки

        :return: возвращает угол положения секундной стрелки в формате float
        """
        return self.second_angle

    def get_year(self) -> int:
        """
        Возвращает текущий год

        :return: возвращает значение года в формате int
        """
        return self.year

    def get_month(self) -> int:
        """
        Возвращает текущий месяц

        :return: возвращает значение месяца в формате int
        """
        return self.month

    def get_day(self) -> int:
        """
        Возвращает текущий день

        :return: возвращает значение дня в формате int
        """
        return self.day

    def get_day_night_division(self) -> DayNightDivision:
        """
        Возвращает время суток

        :return: возвращает значение времени суток в формате DayNightDivision
        """
        return self.day_night_division
