import pytest
from unique_elements import find_unique

def test_basic_case():
    """Тест обычного случая"""
    assert find_unique([1, 2, 3, 2, 4, 1]) == [3, 4]

def test_all_unique():
    """Тест со всеми уникальными элементами"""
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_all_duplicates():
    """Тест со всеми повторяющимися элементами"""
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_empty_list():
    """Тест с пустым списком"""
    assert find_unique([]) == []

def test_strings():
    """Тест со строками"""
    assert find_unique(["a", "b", "a", "c", "b"]) == ["c"]

def test_mixed_types():
    """Тест со смешанными типами"""
    assert find_unique([1, "a", 1, "b", "a"]) == ["b"]

def test_single_element():
    """Тест с одним элементом"""
    assert find_unique([5]) == [5]

def test_multiple_unique():
    """Тест с несколькими уникальными элементами"""
    assert find_unique([1, 2, 3, 4, 5, 1, 2]) == [3, 4, 5]

def test_order_preservation():
    """Тест сохранения порядка первого вхождения"""
    result = find_unique([3, 1, 2, 1, 3, 4])
    assert result == [2, 4]

def test_float_numbers():
    """Тест с числами с плавающей точкой"""
    assert find_unique([1.5, 2.0, 1.5, 3.0]) == [2.0, 3.0]

def test_none_values():
    """Тест с None значениями"""
    assert find_unique([None, 1, None, 2]) == [1, 2]

def test_boolean_values():
    """Тест с булевыми значениями"""
    assert find_unique([True, False, True, False, True]) == []