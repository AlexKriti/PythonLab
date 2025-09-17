text = input("Введите строку: ")
result = ""
vowels = "aeiouAEIOU"

for char in text:
    if char not in vowels:
        result += char

print("Результат:", result)