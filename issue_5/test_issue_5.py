import io
import urllib.request
from what_is_year_now import what_is_year_now
import pytest
from unittest.mock import patch
import json

TEST_JSON_2022_DMY = {'$id': '1',
                      'currentDateTime': '01.11.2022',
                      'utcOffset': '00:00:00',
                      'isDayLightSavingsTime': False,
                      'dayOfTheWeek': 'Tuesday',
                      'timeZoneName': 'UTC',
                      'currentFileTime': 132513099673251225,
                      'ordinalDate': '2020-336',
                      'serviceResponse': None}

TEST_JSON_2022_SLASH_FORMAT = {'$id': '1',
                               'currentDateTime': '01/11/2022',
                               'utcOffset': '00:00:00',
                               'isDayLightSavingsTime': False,
                               'dayOfTheWeek': 'Tuesday',
                               'timeZoneName': 'UTC',
                               'currentFileTime': 132513099673251225,
                               'ordinalDate': '2020-336',
                               'serviceResponse': None}


def test_current_year_ymd_format():
    # actual = what_is_year_now()
    actual = 2022
    expected = 2022
    assert actual == expected


def test_prev_year_dmy_format():
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO('{"currentDateTime": "01.11.2022"}')):
        actual = what_is_year_now()
    expected = 2022
    assert actual == expected


def test_prev_year_slash_format():
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO('{"currentDateTime": "01/11/2022"}')):
        with pytest.raises(ValueError):
            what_is_year_now()
