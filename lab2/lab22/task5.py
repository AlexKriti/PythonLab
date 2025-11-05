# объявляем декоратор, словарь для данных и обертку

def cache(func):
    cache_dict = {} 
    def wrap(*args, **kwargs):

        # создаем ключ для кэша

        key = (args , tuple(sorted(kwargs.items())))

        # проверяем наличия кэша в словаре   

        if key in cache_dict: 
            return cache_dict[key]

        # вычисляем и сохраняем результат в словарь

        else :
            result = func(*args, **kwargs)
            cache_dict[key] = result
        return result
    return wrap

# вызов декоратора

@cache
def test_sum(a,b): 
    if type(a) == type(b):
        return(a+b)
    else:
        print("Types of data are different")

res = test_sum(1 ,2)
print(res)
res = test_sum(a=5, b=11)
print(res)
res = test_sum(a="5", b=11)
print(res)
