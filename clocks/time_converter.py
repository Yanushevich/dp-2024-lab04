from consts import DayNightDivision, TimeConsts


class TimeConverter:
    @staticmethod
    def get_hour_angle(hour: int, minute: int) -> float:
        """
        Возвращает значение угла часовой стрелки, учитывая время в минутах

        :param hour: значение часа в формате int
        :param minute: значение минуты в формате int
        :return: возвращает угол положения часовой стрелки в формате float
        """
        return (TimeConsts.DEG_PER_HOUR * (hour % TimeConsts.AM_PM_DIFF)
                + minute * TimeConsts.MIN_DEG_PER_HOUR)

    @staticmethod
    def get_hour(hour_angle: float, day_night_division: DayNightDivision) -> int:
        """
        Возвращает значение часа

        :param hour_angle: значение угла часовой стрелки в формате float
        :param day_night_division: значение времени суток (AM/PM) в формате DayNightDivision
        :return: возвращает значение времени в часах в формате int
        """
        return (
            int(hour_angle // TimeConsts.DEG_PER_HOUR)
            if (day_night_division == DayNightDivision.AM)
            else (int(hour_angle // TimeConsts.DEG_PER_HOUR) + TimeConsts.AM_PM_DIFF)
        )

    @staticmethod
    def get_minute_angle(minute: int, second: int) -> float:
        """
        Возвращает значение угла минутной стрелки, учитывая время в секундах

        :param minute: значение минуты в формате int
        :param second: значение секунды в формате int
        :return: возвращает угол положения минутной стрелки в формате float
        """
        return minute * TimeConsts.DEG_PER_MIN + second * TimeConsts.SEC_DEG_PER_SEC

    @staticmethod
    def get_minute(minute_angle: float) -> int:
        """
        Возвращает значение минуты

        :param minute_angle: значение угла минутной стрелки в формате float
        :return: возвращает значение времени в минутах в формате int
        """
        return int(minute_angle // TimeConsts.DEG_PER_MIN)

    @staticmethod
    def get_second_angle(second: int) -> float:
        """
        Возвращает значение угла секундной стрелки

        :param second: значение секунды в формате int
        :return: возвращает угол положения секундной стрелки в формате float
        """
        return TimeConsts.DEG_PER_SEC * second

    @staticmethod
    def get_second(second_angle: float) -> int:
        """
        Возвращает значение секунды

        :param second_angle: значение угла секундной стрелки в формате float
        :return: возвращает значение времени в секундах в формате int
        """
        return int(second_angle // TimeConsts.DEG_PER_SEC)

    @staticmethod
    def get_day_night_division(hour: int) -> DayNightDivision:
        """
        Возвращает время суток

        :param hour: значение часа в формате int
        :return: возвращает время суток в формате DayNightDivision
        """
        if hour >= TimeConsts.AM_PM_DIFF:
            return DayNightDivision.PM
        else:
            return DayNightDivision.AM
