def count_words(sentence):
    """
    Функция подсчитывает количество слов в предложении.
    Слова разделяются пробелами.
    
    Args:
        sentence (str): Входная строка с предложением
        
    Returns:
        int: Количество слов в предложении
    """
    if not sentence or not sentence.strip():
        return 0
    
    # Разделяем строку по пробелам и фильтруем пустые строки
    words = [word for word in sentence.split() if word]
    return len(words)


# Тесты с использованием pytest
if __name__ == "__main__":
    # Простые тесты для проверки без pytest
    def test_count_words():
        # Тест 1: Обычное предложение
        assert count_words("Hello world") == 2, "Ошибка в обычном предложении"
        
        # Тест 2: Пустая строка
        assert count_words("") == 0, "Ошибка с пустой строкой"
        
        # Тест 3: Строка только с пробелами
        assert count_words("   ") == 0, "Ошибка со строкой из пробелов"
        
        # Тест 4: Множественные пробелы между словами
        assert count_words("Hello   world   test") == 3, "Ошибка с множественными пробелами"
        
        # Тест 5: Строка с пробелами в начале и конце
        assert count_words("  Hello world  ") == 2, "Ошибка с пробелами по краям"
        
        # Тест 6: Одно слово
        assert count_words("Hello") == 1, "Ошибка с одним словом"
        
        # Тест 7: Специальные символы (считаются частью слов)
        assert count_words("Hello, world! How are you?") == 5, "Ошибка со специальными символами"
        
        # Тест 8: Табуляции и переносы строк
        assert count_words("Hello\tworld\nnew line") == 4, "Ошибка с табуляциями и переносами"
        
        print("Все тесты прошли успешно!")
    
    test_count_words()