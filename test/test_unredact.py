import pytest
from pyredactkit.unredact import Unredactor

key_mapping = {
    "2b21e939-abc9-4d06-9c5a-de9bf2aa22b4": "10.10.10.1"}
redacted_text = "My router is : 2b21e939-abc9-4d06-9c5a-de9bf2aa22b4"
unredacted_text = "My router is : 10.10.10.1"


@pytest.fixture
def unredactor_obj():
    return Unredactor()


def test_replace_all_function_should_return_unredacted_string(unredactor_obj):
    assert unredactor_obj.replace_all(
        redacted_text, key_mapping) == unredacted_text, 'replace_all function should return unredacted string'
