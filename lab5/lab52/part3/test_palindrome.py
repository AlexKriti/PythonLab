import pytest
from palindrome import is_palindrome

def test_word_palindromes():
    """Тест слов-палиндромов"""
    assert is_palindrome("radar") == True
    assert is_palindrome("Level") == True
    assert is_palindrome("deified") == True

def test_word_non_palindromes():
    """Тест слов, не являющихся палиндромами"""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_number_palindromes():
    """Тест чисел-палиндромов"""
    assert is_palindrome(121) == True
    assert is_palindrome(12321) == True
    assert is_palindrome(1221) == True

def test_number_non_palindromes():
    """Тест чисел, не являющихся палиндромами"""
    assert is_palindrome(123) == False
    assert is_palindrome(1234) == False
    assert is_palindrome(12) == False

def test_edge_cases():
    """Тест граничных случаев"""
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
    assert is_palindrome(1) == True
    assert is_palindrome(0) == True

def test_case_insensitivity():
    """Тест нечувствительности к регистру"""
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_ignore_spaces():
    """Тест игнорирования пробелов"""
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw") == True
    assert is_palindrome("No lemon no melon") == True

def test_float_numbers():
    """Тест чисел с плавающей точкой"""
    assert is_palindrome(12.21) == True
    assert is_palindrome(123.321) == True
    assert is_palindrome(12.34) == False

def test_special_cases():
    """Тест специальных случаев"""
    assert is_palindrome("!@#$%$#@!") == True  # Спецсимволы-палиндром
    assert is_palindrome("1234321") == True    # Цифровая строка-палиндром  