# def type_check(*types): 
#     def decorator(func):
#         def wrapper(*args , **kwargs ): 
#             for arg, type in zip(args, types):
#                 if not isinstance(arg, type):
#                     raise TypeError('Несоответсвие типов')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator 


# @type_check(int , int )
# def test_func(a, b ): 
#     return a  + b

# print(test_func(1,2))
# print(test_func("1" , "2"))

def type_check(*expected_types):
    """
    Декоратор для проверки типов аргументов функции.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(
                    f"Несоответствие количества аргументов. "
                    f"Ожидалось: {len(expected_types)}, получено: {len(args)}. "
                    f"Аргументы: {args}"
                )
            
            for i, (arg, expected_type) in enumerate(zip(args, expected_types), 1):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Несоответствие типа для аргумента {i}. "
                        f"Ожидался тип: {expected_type.__name__}, "
                        f"получен тип: {type(arg).__name__}, "
                        f"значение: {repr(arg)}"
                    )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    """Функция сложения двух чисел"""
    return a + b


@type_check(str, int, float)
def person_info(name, age, height):
    """Функция создания информации о человеке"""
    return f"{name}, {age} лет, рост {height} м"


def get_user_choice():
    """Функция для получения выбора пользователя"""
    while True:
        choice = input("\nХотите продолжить? (да/нет): ").strip().lower()
        if choice in ('да', 'д', 'yes', 'y'):
            return True
        elif choice in ('нет', 'н', 'no', 'n'):
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'")


def input_with_validation(prompt, expected_type):
    """
    Функция для ввода данных с валидацией типа
    
    Args:
        prompt: Подсказка для пользователя
        expected_type: Ожидаемый тип данных
    
    Returns:
        Введенное значение в нужном типе или None при ошибке
    """
    while True:
        try:
            user_input = input(prompt)
            
            # Преобразуем ввод в нужный тип
            if expected_type == int:
                value = int(user_input)
            elif expected_type == float:
                value = float(user_input)
            elif expected_type == str:
                value = user_input
            else:
                value = expected_type(user_input)
            
            print(f"✓ Введено: {repr(value)} (тип: {type(value).__name__})")
            return value
            
        except ValueError as e:
            print(f"✗ Ошибка! Ожидался тип {expected_type.__name__}, введено: {repr(user_input)}")
            print(f"  Сообщение об ошибке: {e}")
            
            if not get_user_choice():
                return None


def main():
    """Основная функция программы"""
    print("=" * 60)
    print("ПРОГРАММА ДЛЯ ПРОВЕРКИ ТИПОВ АРГУМЕНТОВ ФУНКЦИЙ")
    print("=" * 60)
    
    while True:
        print("\n" + "-" * 50)
        print("Выберите функцию для тестирования:")
        print("1. Сложение двух чисел (int, int)")
        print("2. Информация о человеке (str, int, float)")
        print("3. Выход")
        
        choice = input("\nВаш выбор (1-3): ").strip()
        
        if choice == "1":
            test_add_function()
        elif choice == "2":
            test_person_info_function()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")
        
        if choice in ("1", "2"):
            if not get_user_choice():
                print("До свидания!")
                break


def test_add_function():
    """Тестирование функции сложения"""
    print("\n--- Тестирование функции сложения ---")
    print("Функция: add(a: int, b: int) -> int")
    
    print("\nВведите первый аргумент (целое число):")
    a = input_with_validation("a = ", int)
    if a is None:
        return
    
    print("\nВведите второй аргумент (целое число):")
    b = input_with_validation("b = ", int)
    if b is None:
        return
    
    print(f"\nВызов функции: add({a}, {b})")
    
    try:
        result = add(a, b)
        print(f"✓ Результат: {result}")
    except TypeError as e:
        print(f"✗ Ошибка типа: {e}")


def test_person_info_function():
    """Тестирование функции информации о человеке"""
    print("\n--- Тестирование функции информации о человеке ---")
    print("Функция: person_info(name: str, age: int, height: float) -> str")
    
    print("\nВведите имя (строка):")
    name = input_with_validation("Имя = ", str)
    if name is None:
        return
    
    print("\nВведите возраст (целое число):")
    age = input_with_validation("Возраст = ", int)
    if age is None:
        return
    
    print("\nВведите рост (дробное число):")
    height = input_with_validation("Рост = ", float)
    if height is None:
        return
    
    print(f"\nВызов функции: person_info({repr(name)}, {age}, {height})")
    
    try:
        result = person_info(name, age, height)
        print(f"✓ Результат: {result}")
    except TypeError as e:
        print(f"✗ Ошибка типа: {e}")


if __name__ == "__main__":
    main()