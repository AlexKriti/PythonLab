def are_anagrams(str1, str2):
    """
    Функция проверяет, являются ли две строки анаграммами.
    Анаграммы - строки, которые содержат одни и те же буквы в разном порядке.
    
    Args:
        str1 (str): Первая строка
        str2 (str): Вторая строка
        
    Returns:
        bool: True если строки являются анаграммами, иначе False
    """
    # Удаляем пробелы и приводим к нижнему регистру
    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()
    
    # Если длины разные, это не анаграммы
    if len(str1_clean) != len(str2_clean):
        return False
    
    # Сортируем символы и сравниваем
    return sorted(str1_clean) == sorted(str2_clean)


# Тесты с использованием pytest
if __name__ == "__main__":
    # Простые тесты для проверки без pytest
    def test_are_anagrams():
        # Тест 1: Очевидные анаграммы
        assert are_anagrams("listen", "silent") == True, "Ошибка с 'listen' и 'silent'"
        assert are_anagrams("triangle", "integral") == True, "Ошибка с 'triangle' и 'integral'"
        
        # Тест 2: Не анаграммы
        assert are_anagrams("hello", "world") == False, "Ошибка с 'hello' и 'world'"
        assert are_anagrams("python", "java") == False, "Ошибка с 'python' и 'java'"
        
        # Тест 3: Анаграммы с разным регистром
        assert are_anagrams("Listen", "Silent") == True, "Ошибка с разным регистром"
        
        # Тест 4: Анаграммы с пробелами
        assert are_anagrams("school master", "the classroom") == True, "Ошибка с пробелами"
        assert are_anagrams("debit card", "bad credit") == True, "Ошибка с пробелами 2"
        
        # Тест 5: Пустые строки
        assert are_anagrams("", "") == True, "Ошибка с пустыми строками"
        
        # Тест 6: Одинаковые строки
        assert are_anagrams("test", "test") == True, "Ошибка с одинаковыми строками"
        
        # Тест 7: Разная длина
        assert are_anagrams("short", "longer") == False, "Ошибка с разной длиной"
        
        # Тест 8: Специальные символы и цифры
        assert are_anagrams("a1b2", "2b1a") == True, "Ошибка с цифрами"
        assert are_anagrams("a!b@", "@b!a") == True, "Ошибка со спецсимволами"
        
        # Тест 9: Фразы-анаграммы
        assert are_anagrams("William Shakespeare", "I am a weakish speller") == True, "Ошибка с фразами"
        
        print("Все тесты прошли успешно!")
    
    test_are_anagrams()