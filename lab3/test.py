# класс Кот(окрас, порода, ) , класс Домашний код(кличка), Гуляющий кот

# методы кошек, спать кушать играть с мышкой/ просить вкусняшку, валить елку/
# переопределение методов

# пользователь при запуске выбирает, с какой кошкой он столкнулся через консольку
# accessible_methods = "sleep, stretch, eat, play, yawn, make_miaow"

class Cat:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    
    def sleep(self):
        print("Кот спит прямо сейчас")
    
    def stretch(self):
        print("Кот потягивается")
    
    def eat(self):
        print("Кот ест")
    
    def play(self):
        print("Кот играет")
    
    def yawn(self):
        print("Кот зевает")
    
    def make_miaow(self):
        print("Кот говорит: - Мяууу.")


class HomeCat(Cat):
    def __init__(self, color, age, breed, name):
        super().__init__(color, age)
        self.breed = breed
        self.name = name
    
    def get_name(self):
        return self.name
    
    def call_cat(self):
        print(f"Вы позвали: '{self.name}, иди сюда!' и кот подошел к вам")
    
    def play(self):
        print(f"{self.name} играет с елкой!")
    
    def ask_for_food(self):
        print(f"{self.name} трется об ногу и говорит: 'Мяу мяу!', так он просит еды")


class StreetCat(Cat):
    def __init__(self, color, age):
        super().__init__(color, age)
        self.name = "Бездомный кот"
    
    def play(self):
        print("Кот играет с мышкой")


def main():
    current_cat = None
    
    while True:
        print("Консольная котовальня\n")
        
        if current_cat:
            if isinstance(current_cat, HomeCat):
                print(f"Текущий кот: {current_cat.name} (Домашний)")
            else:
                print(f"Текущий кот: {current_cat.name}")
            print(f"Цвет: {current_cat.color}, Возраст: {current_cat.age}")
            if isinstance(current_cat, HomeCat):
                print(f"Порода: {current_cat.breed}")
        else:
            print("Кот не выбран")
        
        print("\nДоступные действия:")
        print("0. Выйти")
        print("1. Выбрать домашнего кота")
        print("2. Выбрать уличного кота")
        
        if current_cat:
            print("3. Уложить спать")
            print("4. Покормить")
            print("5. Поиграть")
            print("6. Позвать кота (только для домашнего)")
            print("7. Попросить еды (только для домашнего)")
            print("8. Потягивание")
            print("9. Зевок")
            print("10. Помяукать")
            print("11. Сменить кота")
        
        
        
        choice = input("\nВыберите действие: ")
        
        if choice == "0":
            print("Выход из приложения...")
            break
        
        elif choice == "1":
            print("\nСоздаем домашнего кота:")
            name = input("Введите кличку кота: ")
            color = input(f"Введите цвет {name}: ")
            age = input(f"Введите возраст {name}: ")
            breed = input(f"Введите породу {name}: ")
            current_cat = HomeCat(color, age, breed, name)
            print(f"\nСоздан домашний кот {name}!")
        
        elif choice == "2":
            print("\nСоздаем уличного кота:")
            color = input("Введите цвет кота: ")
            age = input("Введите возраст кота: ")
            current_cat = StreetCat(color, age)
            print(f"\nСоздан уличный кот!")
        
        elif current_cat:
            if choice == "3":
                current_cat.sleep()
            elif choice == "4":
                current_cat.eat()
            elif choice == "5":
                current_cat.play()
            elif choice == "6":
                if isinstance(current_cat, HomeCat):
                    current_cat.call_cat()
                else:
                    print("Этот метод доступен только для домашних котов!")
            elif choice == "7":
                if isinstance(current_cat, HomeCat):
                    current_cat.ask_for_food()
                else:
                    print("Этот метод доступен только для домашних котов!")
            elif choice == "8":
                current_cat.stretch()
            elif choice == "9":
                current_cat.yawn()
            elif choice == "10":
                current_cat.make_miaow()
            elif choice == "11":
                current_cat = None
                print("Кот сброшен. Выберите нового кота.")
            else:
                print("Неверный выбор!")
        else:
            print("Сначала выберите кота!")
        
        if current_cat and choice in ["3", "4", "5", "6", "7", "8", "9", "10"]:
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
