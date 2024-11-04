from datetime import datetime
import clocks


def main():
    # Создаем объект для хранения даты в аналоговом формате
    analog_clock = clocks.AnalogClock()
    # Создаем объект адаптера, передавая ему объект для хранения
    digital_clock = clocks.DigitalClockAdapter(analog_clock)
    # Задаем дату в цифровом формате
    digital_clock.set_date_time(datetime(2024, 11, 4, 5, 59, 31))
    # Проверим данные в цифровом формате
    print(digital_clock.get_date_time())
    # Проверим данные в аналоговом формате
    print(analog_clock.get_year(), analog_clock.get_month(), analog_clock.get_day())
    print(analog_clock.get_hour_angle())
    print(analog_clock.get_minute_angle())
    print(analog_clock.get_second_angle())
    print(analog_clock.day_night_division)


if __name__ == "__main__":
    main()
