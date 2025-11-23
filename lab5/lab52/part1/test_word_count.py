import pytest
from word_count import count_words

def test_basic_sentence():
    """Тест обычного предложения"""
    assert count_words("Hello world") == 2

def test_empty_string():
    """Тест пустой строки"""
    assert count_words("") == 0

def test_only_spaces():
    """Тест строки только с пробелами"""
    assert count_words("   ") == 0

def test_multiple_spaces():
    """Тест с множественными пробелами между словами"""
    assert count_words("Hello   world   test") == 3

def test_leading_trailing_spaces():
    """Тест с пробелами в начале и конце"""
    assert count_words("  Hello world  ") == 2

def test_single_word():
    """Тест с одним словом"""
    assert count_words("Hello") == 1

def test_special_characters():
    """Тест со специальными символами"""
    assert count_words("Hello, world! How are you?") == 5

def test_tabs_and_newlines():
    """Тест с табуляциями и переносами строк"""
    assert count_words("Hello\tworld\nnew line") == 4

def test_mixed_whitespace():
    """Тест со смешанными пробельными символами"""
    assert count_words("Hello \t world \n test") == 3

def test_numbers_and_words():
    """Тест с числами и словами - ИСПРАВЛЕННЫЙ ТЕСТ"""
    # В строке "I have 2 apples and 3 oranges" действительно 7 слов:
    # I, have, 2, apples, and, 3, oranges
    assert count_words("I have 2 apples and 3 oranges") == 7