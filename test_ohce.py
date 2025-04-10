from ohce import Ohce
from datetime import datetime
import pytest

def test_greeting_morning(monkeypatch):
    def mock_now():
        return datetime(2025, 4, 9, 10, 0)
    monkeypatch.setattr("ohce.datetime.now", mock_now)
    ohce = Ohce("Pedro")
    assert ohce.greet() == "¡Buenos días Pedro!"