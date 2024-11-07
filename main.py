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
    print("Дата -", analog_clock.get_year(), analog_clock.get_month(), analog_clock.get_day())
    print(f"Угол часовой стрелки - {analog_clock.get_hour_angle()}")
    print(f"Угол минутной стрелки - {analog_clock.get_minute_angle()}")
    print(f"Угол секундной стрелки - {analog_clock.get_second_angle()}")
    print(f"Время суток (AM/PM) - {analog_clock.day_night_division.value}")


if __name__ == "__main__":
    main()
