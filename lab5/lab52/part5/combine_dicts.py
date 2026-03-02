def combine_dicts(dict1, dict2):
    """
    Функция объединяет два словаря, сохраняя порядок следования элементов.
    При совпадении ключей приоритет отдается значениям из второго словаря.
    
    Args:
        dict1 (dict): Первый словарь
        dict2 (dict): Второй словарь
        
    Returns:
        dict: Новый словарь, содержащий все элементы из обоих словарей
    """
    result = dict1.copy()  # Создаем копию первого словаря
    
    # Добавляем элементы из второго словаря
    # При совпадении ключей значения из второго словаря перезаписывают значения из первого
    for key, value in dict2.items():
        result[key] = value
    
    return result


# Тесты с использованием pytest
if __name__ == "__main__":
    # Простые тесты для проверки без pytest
    def test_combine_dicts():
        # Тест 1: Обычное объединение
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        assert combine_dicts(dict1, dict2) == expected, "Ошибка обычного объединения"
        
        # Тест 2: Перекрывающиеся ключи
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        assert combine_dicts(dict1, dict2) == expected, "Ошибка с перекрывающимися ключами"
        
        # Тест 3: Пустые словари
        assert combine_dicts({}, {}) == {}, "Ошибка с пустыми словарями"
        assert combine_dicts({'a': 1}, {}) == {'a': 1}, "Ошибка с одним пустым словарем"
        assert combine_dicts({}, {'b': 2}) == {'b': 2}, "Ошибка с одним пустым словарем"
        
        # Тест 4: Вложенные словари
        dict1 = {'a': {'x': 1}, 'b': 2}
        dict2 = {'a': {'y': 2}, 'c': 3}
        result = combine_dicts(dict1, dict2)
        expected = {'a': {'y': 2}, 'b': 2, 'c': 3}
        assert result == expected, "Ошибка с вложенными словарями"
        
        # Тест 5: Разные типы значений
        dict1 = {'a': 1, 'b': 'hello'}
        dict2 = {'c': [1, 2, 3], 'd': None}
        expected = {'a': 1, 'b': 'hello', 'c': [1, 2, 3], 'd': None}
        assert combine_dicts(dict1, dict2) == expected, "Ошибка с разными типами"
        
        # Тест 6: Сохранение порядка (проверяем порядок ключей)
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'d': 4, 'e': 5}
        result = combine_dicts(dict1, dict2)
        # В Python 3.7+ порядок ключей сохраняется
        keys = list(result.keys())
        expected_keys = ['a', 'b', 'c', 'd', 'e']
        assert keys == expected_keys, f"Ошибка сохранения порядка: {keys} != {expected_keys}"
        
        print("Все тесты прошли успешно!")
    
    test_combine_dicts()