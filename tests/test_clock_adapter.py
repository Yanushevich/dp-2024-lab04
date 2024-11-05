from datetime import datetime
import unittest
import clocks


class TestClockAdapter(unittest.TestCase):
    def setUp(self):
        self.analog_clock = clocks.AnalogClock()
        self.digital_clock_adapter = clocks.DigitalClockAdapter(self.analog_clock)
        self.digital_clock_adapter.set_date_time(datetime(2024, 12, 31, 18, 30, 3))

    def test_year(self):
        """Проверка правильного сохранения значения года"""
        self.assertEqual(self.analog_clock.get_year(), 2024)

    def test_month(self):
        """Проверка правильного сохранения значения месяца"""
        self.assertEqual(self.analog_clock.get_month(), 12)

    def test_day(self):
        """Проверка правильного сохранения значения дня"""
        self.assertEqual(self.analog_clock.get_day(), 31)

    def test_hour_angle(self):
        """
        Учитывая, что:
        за каждый час часовая стрелка проходит угол в 360/12 = 30 градусов,
        за каждую минуту - угол в 30/60 = 0.5 градуса,
        заданное время - 6 часов 30 минут,
        проверяем, равен ли угол часовой стрелки 6 * 30 + 30 * 0.5 = 195 градусов
        """
        self.assertEqual(self.analog_clock.get_hour_angle(), 195.0)

    def test_minute_angle(self):
        """
        Учитывая, что:
        за каждую минуту минутная стрелка проходит угол в 360/60 = 6 градусов,
        за каждую секунду - угол в 6/60 = 0.1 градуса,
        заданное время - 30 минут 3 секунды,
        проверяем, равен ли угол минутной стрелки 30 * 6 + 3 * 0.1 = 180.3 градусов
        """
        self.assertEqual(self.analog_clock.get_minute_angle(), 180.3)

    def test_second_angle(self):
        """
        Учитывая, что за каждую секунду секундная стрелка проходит угол в 360/60 = 6 градусов,
        заданное время - 3 секунды,
        проверяем, равен ли угол секундной стрелки 6 * 3 = 18
        """
        self.assertEqual(self.analog_clock.get_second_angle(), 18.0)

    def test_digital_clock_return_type(self):
        """Проверяем, равен ли тип возвращаемого значения адаптера типу datetime"""
        self.assertIsInstance(self.digital_clock_adapter.get_date_time(), datetime)


if __name__ == '__main__':
    unittest.main()
