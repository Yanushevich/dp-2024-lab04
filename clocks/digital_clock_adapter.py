from datetime import datetime
from interfaces import BaseDigitalClock, BaseAnalogClock
from consts import DayNightDivision


class DigitalClockAdapter(BaseDigitalClock):
    def __init__(self, analog_clock: BaseAnalogClock):
        self._analog_clock = analog_clock
        self.date = None

    def get_hour_angle(self) -> int:
        return 30 * (self.date.hour % 12) + self.date.minute * 0.5

    def get_hour(self) -> int:
        return (
            int(self._analog_clock.get_hour_angle() // 30)
            if (self.get_day_night_division() == DayNightDivision.AM)
            else (int(self._analog_clock.get_hour_angle() // 30) + 12)
        )

    def get_minute_angle(self) -> int:
        return 6 * self.date.minute + self.date.second * 0.1

    def get_minute(self) -> int:
        return int(self._analog_clock.get_minute_angle() // 6)

    def get_second_angle(self) -> int:
        return 6 * self.date.second

    def get_second(self) -> int:
        return int(self._analog_clock.get_second_angle() // 6)

    def get_day_night_division(self):
        if self.date.hour > 11:
            return DayNightDivision.PM
        else:
            return DayNightDivision.AM

    def set_date_time(self, date: datetime) -> None:
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
        return datetime(
            self._analog_clock.get_year(),
            self._analog_clock.get_month(),
            self._analog_clock.get_day(),
            self.get_hour(),
            self.get_minute(),
            self.get_second(),
        )
