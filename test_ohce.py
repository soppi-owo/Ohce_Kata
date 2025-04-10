from ohce import Ohce
from datetime import datetime

def test_greeting_morning(mocker):
    mocked_datetime = mocker.patch("ohce.datetime")
    mocked_datetime.now.return_value = datetime(2025, 4, 9, 10, 0)  # 10:00
    ohce = Ohce("Pedro")
    assert ohce.greet() == "¡Buenos días Pedro!"

def test_greeting_afternoon(mocker):
    mocked_datetime = mocker.patch("ohce.datetime")
    mocked_datetime.now.return_value = datetime(2025, 4, 9, 15, 0)  # 15:00
    ohce = Ohce("Pedro")
    assert ohce.greet() == "¡Buenas tardes Pedro!"

def test_greeting_night(mocker):
    mocked_datetime = mocker.patch("ohce.datetime")
    mocked_datetime.now.return_value = datetime(2025, 4, 9, 22, 0)  # 22:00
    ohce = Ohce("Pedro")
    assert ohce.greet() == "¡Buenas noches Pedro!"