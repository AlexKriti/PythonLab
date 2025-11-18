# Ввод данных
set1 = set(map(float, input("Введите первый набор чисел через пробел: ").split()))
set2 = set(map(float, input("Введите второй набор чисел через пробел: ").split()))

# общие числа
common = set1 & set2
print("Числа в обоих наборах:", sorted(common))

# уникальные числа для каждого набора
unique_to_set1 = set1 - set2
unique_to_set2 = set2 - set1
print("Числа только в первом наборе:", sorted(unique_to_set1))
print("Числа только во втором наборе:", sorted(unique_to_set2))

# числа, не являющиеся общими
non_common = set1 ^ set2
print("Числа, исключая общие:", sorted(non_common))