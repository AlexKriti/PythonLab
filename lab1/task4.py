# Запрос данных у пользователя
numstr = input("Ввеедите число: ")

#переведем число из формата строки в формат числа
num = int(numstr)

#для каждого разделения купюр/монет найдем нужное количество и 
#сразу переведем в строку для последующей конкатенации
hundreds = str(num//100)
num = num%100
fifties = str(num//50)
num = num%50
tenth = str(num//10)
num = num%10
fifth = str(num//5)
num = num%5
second = str(num//2)
num = num%2
first = str(num//1)
print("Понадобится "+hundreds+" купюр по 100, "+fifties+" купюр по 50, "+tenth+" купюр по 10, "+fifth+" купюр по 5, "+second+" монет по 2, "+first+" монет по 1")