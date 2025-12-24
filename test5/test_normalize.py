import pytest
from normalize import normalize

#Fixtures
@pytest.fixture
def simple_list():
    return [0, 5, 10]

@pytest.fixture
def list_with_none():
    return [2, None, 4, 6]

#Parametrized tests
@pytest.mark.parametrize(
    "values, expected",
    [
        ([0, 5, 10], [0.0, 0.5, 1.0]),
        ([1, 2, 3], [0.0, 0.5, 1.0]),
        ([-5, 0, 5], [0.0, 0.5, 1.0]),
    ]
)

def test_normalize_basic(values, expected):
    assert normalize(values) == expected

def test_normalize_with_fixture(simple_list):
    assert normalize(simple_list) == [0.0, 0.5, 1.0]

def test_normalize_with_none(list_with_none):
    assert normalize(list_with_none) == [0.0, None, 0.5, 1.0]

#Exception tests
@pytest.mark.edge
@pytest.mark.parametrize(
    "values",
    [
        [],
        [None, None],
        [5, 5, 5],
    ]
)
def test_normalize_errors(values):
    with pytest.raises(ValueError):
        normalize(values)

#Marked test
@pytest.mark.slow
def test_large_input():
    data = list(range(100000))
    result = normalize(data)
    assert result[0] == 0.0
    assert result[-1] == 1.0
