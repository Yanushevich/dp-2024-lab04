from datetime import datetime
import clocks


def main():
    analog_clock = clocks.AnalogClock()
    digital_clock = clocks.DigitalClockAdapter(analog_clock)
    digital_clock.set_date_time(datetime(2024, 11, 4, 5, 59, 31))
    print(digital_clock.get_date_time())
    print(analog_clock.get_hour_angle())
    print(analog_clock.get_minute_angle())
    print(analog_clock.get_second_angle())


if __name__ == "__main__":
    main()
