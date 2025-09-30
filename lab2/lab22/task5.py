# объявляем декоратор, словарь для данных и обертку

def cache(func):
    cache_dictionary = {} 
    def wrap(*args, **kwargs):

        # создаем ключ для кэша

        key = (args , tuple(sorted(kwargs.items())))

        # проверяем наличия кэша в словаре   

        if key in cache_dictionary: 
            return cache_dictionary[key]

        # вычисляем и сохраняем результат в словарь

        else :
            result = func(*args, **kwargs)
            cache_dictionary[key] = result
        return result
    return wrap

# вызов декоратора

@cache
def test_sum(a,b): 
    return(a+b)

res = test_sum(1 ,2 )
print(res)