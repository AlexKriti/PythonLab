import time

# объявляем декоратор

def processing_time(func):

    # объявляем функцию-обертку

    def wrap(*args, **kwargs):

        # замеряем время начала выполнения

        start_time = time.perf_counter()

        # вызов основной функции

        result = func(*args, **kwargs)

        # замеряем время конца выполнения и вычисляем разницу

        end_time = time.perf_counter()
        diff_time = (end_time - start_time) * 1000

        # выводим разницу на экран и возвращаем результат

        print(f"Время выполнения функции : {diff_time} мс")
        return result

    # возврат обертки

    return wrap

# вызываем функцию для примера

@processing_time
def test_function(n):
    time.sleep(1)

test_function(1000000)