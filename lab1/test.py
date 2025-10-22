# если длина строки >20 но меньше < 50
# найти частное деления ее длина на 2
# в противном случае если она состоит из букв и цифр, заменить 1 на букву а и вывести каждый третий символ
# иначе напечатать no no no mister fish
string = input("Enter your string: ")
if len(string) > 20 and len(string) < 50:
    print(len(string)//2)
else:
    if not string.isdigit() and not string.isalpha():
        new_str = string.replace("1", "a", len(string))
        print(new_str)
        print(new_str[2::3])
    else:
        print('no no no mister fish')