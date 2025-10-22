# Запрос данных у пользователя
secname = input("Введите свою фамилию:")
name = input("Введите свое имя:")
surname = input("Введите свое отчество:")

#обращение к элементам строки по индексу
print(secname.title() + " " +name[0].upper() + ". " + surname[0].upper() +".")
