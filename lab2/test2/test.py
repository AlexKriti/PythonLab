# генерировать автомобильные номера, проверять на уникальность
import random
letters = ["A", "B" ,"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num_base = set([])
def write_nums(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            number = func(*args, **kwargs)
            if number[len(number) - 1] == "0":
                print("Your in the army now!")
                with open(filename, 'a') as f:
                    f.write("Your in the army now!\n")
                return 
            if number in num_base:
                print("Номера повторились.")
                return 
            else:
                num_base.add(number)
                with open(filename, 'a') as f:
                    f.write(f"{number}\n")
            return number
        return wrapper
    return decorator


@write_nums('testnum.txt')
def generate_num(num_base):
    num = ""
    for i in range(4):
        num += str(int(random.random()*10))
    num += "-" 
    num += letters[int(random.random()*len(letters))]
    num += letters[int(random.random()*len(letters))]
    num += "-" 
    reg = int(random.random()*8.9)
    num += str(reg)
    return num
    
    
    




    
generate_num(num_base)
generate_num(num_base)
generate_num(num_base)
generate_num(num_base)
print(num_base)