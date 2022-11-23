import pytest
from morse import decode


@pytest.mark.parametrize('actual, expected', [
 ('SLIM/SHADY', '... .-.. .. -- -..-. ... .... .- -.. -.--'),
 ('WEEKEND777', '.-- . . -.- . -. -..   --... --... --... '),
 ('1', '.----'),
 ('?MIKHAIL?/', '..--.. -- .. -.- .... .- .. .-.. ..--..   -..-.')
])
def test_decode_correct_string(actual, expected):
    assert actual == decode(expected)
