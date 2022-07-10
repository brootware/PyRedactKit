import pytest
import json
import os
from pyredactkit.common_jobs import CommonJobs


@pytest.fixture
def common_obj():
    return CommonJobs()


@pytest.fixture
def mocker_text_file(mocker):
    content = "Message to write on file to be written"
    mocked_open = mocker.mock_open(read_data=content)
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_open)


def test_write_hashmap_should_create_json_file(common_obj, tmp_path):
    hash_map = {"key": "value"}
    common_obj.write_hashmap(hash_map, filename='fakefile', savedir=tmp_path)
    assert os.path.isfile(f"{tmp_path}.hashshadow_fakefile.json"), f"{tmp_path}.hashshadow_fakefile.json file not created"


def test_valid_options_should_return_tuple(common_obj):
    assert isinstance(common_obj.valid_options(), tuple), "valid_options should return a tuple"


def test_compute_total_words_should_return_int(common_obj, mocker_text_file):
    assert isinstance(common_obj.compute_total_words(filename='fakefile'), int), "compute_total_words should return an int"


def test_compute_reading_minutes_should_return_int(common_obj, mocker_text_file):
    total_words = common_obj.compute_total_words(filename='fakefile')
    assert isinstance(common_obj.compute_reading_minutes(total_words), int), "compute_reading_minutes should return an int"


def test_compute_reading_hours_should_return_int(common_obj, mocker_text_file):
    total_words = common_obj.compute_total_words(filename='fakefile')
    reading_minutes = common_obj.compute_reading_minutes(total_words)
    assert isinstance(common_obj.compute_reading_hours(reading_minutes), int),  "compute_reading_hours should return an int"
