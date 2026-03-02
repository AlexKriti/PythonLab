import pytest
from combine_dicts import combine_dicts

def test_basic_combination():
    """Тест обычного объединения"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert combine_dicts(dict1, dict2) == expected

def test_overlapping_keys():
    """Тест с перекрывающимися ключами"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 3, 'c': 4}
    assert combine_dicts(dict1, dict2) == expected

def test_empty_dicts():
    """Тест с пустыми словарями"""
    assert combine_dicts({}, {}) == {}
    assert combine_dicts({'a': 1}, {}) == {'a': 1}
    assert combine_dicts({}, {'b': 2}) == {'b': 2}

def test_nested_dicts():
    """Тест с вложенными словарями"""
    dict1 = {'a': {'x': 1}, 'b': 2}
    dict2 = {'a': {'y': 2}, 'c': 3}
    result = combine_dicts(dict1, dict2)
    expected = {'a': {'y': 2}, 'b': 2, 'c': 3}
    assert result == expected

def test_different_value_types():
    """Тест с разными типами значений"""
    dict1 = {'a': 1, 'b': 'hello'}
    dict2 = {'c': [1, 2, 3], 'd': None}
    expected = {'a': 1, 'b': 'hello', 'c': [1, 2, 3], 'd': None}
    assert combine_dicts(dict1, dict2) == expected

def test_order_preservation():
    """Тест сохранения порядка ключей"""
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'d': 4, 'e': 5}
    result = combine_dicts(dict1, dict2)
    keys = list(result.keys())
    expected_keys = ['a', 'b', 'c', 'd', 'e']
    assert keys == expected_keys

def test_complex_overlap():
    """Тест сложного перекрытия ключей"""
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict2 = {'c': 5, 'd': 6, 'e': 7, 'f': 8}
    result = combine_dicts(dict1, dict2)
    expected = {'a': 1, 'b': 2, 'c': 5, 'd': 6, 'e': 7, 'f': 8}
    assert result == expected

def test_immutability():
    """Тест неизменяемости исходных словарей"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict1_original = dict1.copy()
    dict2_original = dict2.copy()
    
    combine_dicts(dict1, dict2)
    
    assert dict1 == dict1_original, "Исходный словарь dict1 был изменен"
    assert dict2 == dict2_original, "Исходный словарь dict2 был изменен"