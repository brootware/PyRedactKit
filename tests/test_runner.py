import pytest
from pyredactkit import runner as Runner


@pytest.fixture
def mocker_text_file(mocker):
    content = "Message to write on file to be written"
    mocked_open = mocker.mock_open(read_data=content)
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_open)


def test_is_it_file(mocker_text_file, tmp_path):
    assert Runner.is_it_file('This is a test string') is False, "is_it_file function should return False for this string"


def test_recursive_file_search(mocker_text_file, tmp_path):
    assert Runner.recursive_file_search('This is a test string', 'txt', True) == set(), "recursive_file_search function should return an empty set"


def test_api_identify_sensitive_data(mocker_text_file, tmp_path):
    test_string = """this is my IP: 102.23.5.1
    My router is : 10.10.10.1
    71.159.188.33
    81.141.167.45
    165.65.59.139
    64.248.67.225
    https://tech.gov.sg
    My email is harold@mail.com
    this is my IP: 102.23.5.1
    My router is: 10.10.10.1
    71.159.188.33
    81.141.167.45
    165.65.59.139
    64.248.67.225
    Base64 data
    QVBJX1RPS0VO
    UzNjcjN0UGFzc3dvcmQ=
    U3VwM3JTM2NyZXRQQHNzd29yZA==
    Singapore NRIC
    G0022121F
    F2121200F
    G1021022E
    S1022221L
    G1222221C
    S0000212Q
    F2120212E
    S0021001P
    """
    test_data = ['102.23.5.1', '10.10.10.1', '71.159.188.33', '81.141.167.45', '165.65.59.139', '64.248.67.225', 'https://tech.gov.sg', 'harold@mail.com', 'mail.com', '102.23.5.1', '10.10.10.1', '71.159.188.33', '81.141.167.45', '165.65.59.139', '64.248.67.225', 'QVBJX1RPS0VO', 'UzNjcjN0UGFzc3dvcmQ=', 'U3VwM3JTM2NyZXRQQHNzd29yZA==', 'G0022121F', 'F2121200F', 'G1021022E', 'S1022221L', 'G1222221C', 'S0000212Q', 'F2120212E', 'S0021001P']

    assert Runner.api_identify_sensitive_data(test_string) == test_data, "api_identify_sensitive_data function should return an empty set"
    assert Runner.api_identify_sensitive_data('This is a test string') == [], "api_identify_sensitive_data function should return an empty list"