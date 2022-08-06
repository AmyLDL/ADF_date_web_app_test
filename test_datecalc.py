
def duration():
    pass

def when():
    pass

def test_tautology():
    assert 5 == 3+2

from datecalc import duration
from datecalc import when
import datetime
from datetime import date
from datetime import timedelta

def test_zero_duration ():
    # Arrange
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()
    expected_duration = 0

    # Act
    final_duration = duration(start_date, end_date)

    # Assert
    assert final_duration == expected_duration

def test_10day_duration ():
    # Arrange
    start_date = datetime.date(2022,8,5)
    end_date = datetime.date(2022,8,15)
    expected_duration = 10

    # Act
    final_duration = duration(start_date, end_date)

    # Assert
    assert final_duration == expected_duration

def test_35day_duration ():
    # Arrange
    start_date = datetime.datetime(2022,8,5)
    end_date = datetime.datetime(2022,9,9)
    expected_duration = 35

    # Act
    final_duration = duration(start_date, end_date)

    # Assert
    assert final_duration == expected_duration

