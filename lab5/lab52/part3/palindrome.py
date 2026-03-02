def is_palindrome(value):
    """
    Функция проверяет, является ли переданное значение (слово или число) палиндромом.
    
    Args:
        value: Слово (str) или число (int/float) для проверки
        
    Returns:
        bool: True если значение палиндром, иначе False
    """
    # Преобразуем значение в строку для универсальной обработки
    str_value = str(value).lower().replace(" ", "")
    
    # Сравниваем строку с её перевернутой версией
    return str_value == str_value[::-1]


# Тесты с использованием pytest
if __name__ == "__main__":
    # Простые тесты для проверки без pytest
    def test_is_palindrome():
        # Тест 1: Палиндромы-слова
        assert is_palindrome("radar") == True, "Ошибка с 'radar'"
        assert is_palindrome("Level") == True, "Ошибка с 'Level'"
        assert is_palindrome("A man a plan a canal Panama") == True, "Ошибка с фразой-палиндромом"
        
        # Тест 2: Не палиндромы-слова
        assert is_palindrome("hello") == False, "Ошибка с 'hello'"
        assert is_palindrome("world") == False, "Ошибка с 'world'"
        
        # Тест 3: Палиндромы-числа
        assert is_palindrome(121) == True, "Ошибка с числом 121"
        assert is_palindrome(12321) == True, "Ошибка с числом 12321"
        
        # Тест 4: Не палиндромы-числа
        assert is_palindrome(123) == False, "Ошибка с числом 123"
        assert is_palindrome(1234) == False, "Ошибка с числом 1234"
        
        # Тест 5: Граничные случаи
        assert is_palindrome("a") == True, "Ошибка с одним символом"
        assert is_palindrome("") == True, "Ошибка с пустой строкой"
        assert is_palindrome(1) == True, "Ошибка с числом 1"
        assert is_palindrome(0) == True, "Ошибка с числом 0"
        
        # Тест 6: Регистр и пробелы
        assert is_palindrome("Madam") == True, "Ошибка с регистром"
        assert is_palindrome("Was it a car or a cat I saw") == True, "Ошибка с пробелами"
        
        # Тест 7: Числа с плавающей точкой (преобразуются в строку)
        assert is_palindrome(12.21) == True, "Ошибка с числом 12.21"
        
        print("Все тесты прошли успешно!")
    
    test_is_palindrome()