import pytest
from one_hot_encoder import fit_transform


def test_list_strings():
    test_list = ['slim', 'shady', 'party', 'norimyxxxo']
    actual = fit_transform(test_list)
    expected = [('slim', [0, 0, 0, 1]),
                ('shady', [0, 0, 1, 0]),
                ('party', [0, 1, 0, 0]),
                ('norimyxxxo', [1, 0, 0, 0])]
    assert actual == expected


def test_empty():
    with pytest.raises(TypeError) as cm:
        fit_transform()
    error = cm.value
    assert isinstance(error, TypeError)


def test_string():
    test_list = ['another', 'one']
    container = fit_transform(test_list)
    member = ('one', [1, 0])
    assert member in container


def test_empty_list():
    empty_list = []
    actual = fit_transform(empty_list)
    assert bool(actual) is False
