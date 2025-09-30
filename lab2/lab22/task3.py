import datetime

# описываем функции(фабрика, декоратор, обертка)

def calling_logs(filename):
    def decorator(func):
        def wrap(*args, **kwargs):

            # форматирование в строку "2024-01-15 14:30:25"

            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # форматирование аргументов [1, 12] => "1, 12", {} => ""

            args_str = ", ".join([str(arg) for arg in args])
            kwargs_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])  

            # объединяем аргументы

            all_args = ", ".join(filter(None, [args_str, kwargs_str]))    

            # записываем в файл

            with open(filename, 'a') as f:
                f.write(f"{time_now} - {func.__name__}({all_args})\n")

            # вызываем оригинальную функцию

            return func(*args, **kwargs)
        return wrap
    return decorator

# тестовая запись

@calling_logs("test.txt")
def test(a , b = 10 ):
    return  a + b

test (1, 12 )
