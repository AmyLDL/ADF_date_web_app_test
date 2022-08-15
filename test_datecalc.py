
def duration():
    pass

def when():
    pass

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

def test_when_zero ():
    # Arrange
    start_date = datetime.date.today()
    days_between = 0
    expected_when = start_date

    # Act
    final_when = when(start_date, days_between)

    # Assert
    assert final_when == expected_when

def test_when_add_10days ():
    # Arrange
    start_date = datetime.date(2022,8,8)
    days_between = 10
    expected_when = datetime.date(2022,8,18)

    # Act
    final_when = when(start_date, days_between)

    # Assert
    assert final_when == expected_when

def test_when_add_100days ():
    # Arrange
    start_date = datetime.date(2022,8,8)
    days_between = 100
    expected_when = datetime.date(2022,11,16)

    # Act
    final_when = when(start_date, days_between)

    # Assert
    assert final_when == expected_when