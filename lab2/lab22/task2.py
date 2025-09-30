# определяем функцию для слияния словарей

def merge_dicts(fir_dict, sec_dict):
    for key, value in sec_dict.items():

        # рассматриваем случай наличия ключа в обоих словарях

        if key in fir_dict:

            # для каждого отдельного варианта описыаем свой вариант слияния

            if isinstance(fir_dict[key], dict) and isinstance(value, dict):
                merge_dicts(fir_dict[key], value)
            elif isinstance(fir_dict[key], list) and isinstance(value, list):
                fir_dict[key].extend(value)    
            
            elif isinstance(fir_dict[key], set) and isinstance(value, set):
                fir_dict[key].update(value)
            
            elif isinstance(fir_dict[key], tuple) and isinstance(value, tuple):
                fir_dict[key] = fir_dict[key] + value
            else:
                fir_dict[key] = value

        # если ключа нет во втором словаре, добавляем

        else:
            fir_dict[key] = value

# проверяем на значениях

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)  