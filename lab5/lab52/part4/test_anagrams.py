import pytest
from anagrams import are_anagrams

def test_obvious_anagrams():
    """Тест очевидных анаграмм"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True
    assert are_anagrams("evil", "vile") == True

def test_non_anagrams():
    """Тест не анаграмм"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False
    assert are_anagrams("apple", "pale") == False

def test_case_insensitivity():
    """Тест нечувствительности к регистру"""
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("RACE", "care") == True

def test_with_spaces():
    """Тест анаграмм с пробелами"""
    assert are_anagrams("school master", "the classroom") == True
    assert are_anagrams("debit card", "bad credit") == True
    assert are_anagrams("eleven plus two", "twelve plus one") == True

def test_edge_cases():
    """Тест граничных случаев"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "a") == True
    assert are_anagrams("a", "b") == False

def test_same_strings():
    """Тест одинаковых строк"""
    assert are_anagrams("test", "test") == True
    assert are_anagrams("python", "python") == True

def test_different_lengths():
    """Тест строк разной длины"""
    assert are_anagrams("short", "longer") == False
    assert are_anagrams("abc", "abcd") == False

def test_special_characters():
    """Тест со специальными символами и цифрами"""
    assert are_anagrams("a1b2", "2b1a") == True
    assert are_anagrams("a!b@", "@b!a") == True
    assert are_anagrams("123", "321") == True

def test_famous_anagrams():
    """Тест известных анаграмм"""
    assert are_anagrams("William Shakespeare", "I am a weakish speller") == True
    assert are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort") == True

def test_unicode_characters():
    """Тест с юникод символами"""
    assert are_anagrams("café", "éfac") == True
    assert are_anagrams("café", "cafe") == False  # Разные символы  