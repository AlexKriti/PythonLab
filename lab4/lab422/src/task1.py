import numpy as np

def analyze_transport_expenses():
    """
    Анализирует расходы на проезд по месяцам и сравнивает зимний и летний периоды.
    Находит месяцы с наибольшими расходами.
    """
    
    # Создаем массив расходов на проезд по месяцам (январь - декабрь)
    # Для примера используем случайные данные, можно заменить на реальные
    np.random.seed(42)  # Для воспроизводимости результатов
    expenses = np.random.randint(2000, 5000, 12)
    
    print("=== АНАЛИЗ РАСХОДОВ НА ПРОЕЗД ===")
    print(f"Расходы по месяцам: {expenses}")
    print()
    
    # Индексы месяцев (0-11 соответствуют январь-декабрь)
    months = np.arange(1, 13)
    
    # Зимние месяцы: декабрь (12), январь (1), февраль (2)
    winter_months = [12, 1, 2]
    winter_indices = [11, 0, 1]  # Индексы в массиве (0-based)
    
    # Летние месяцы: июнь (6), июль (7), август (8)
    summer_months = [6, 7, 8]
    summer_indices = [5, 6, 7]  # Индексы в массиве (0-based)
    
    # Суммы расходов по периодам
    winter_total = np.sum(expenses[winter_indices])
    summer_total = np.sum(expenses[summer_indices])
    
    print("=== СРАВНЕНИЕ ПЕРИОДОВ ===")
    print(f"Зимние месяцы {winter_months}: общие расходы = {winter_total} руб.")
    print(f"Летние месяцы {summer_months}: общие расходы = {summer_total} руб.")
    
    if winter_total > summer_total:
        print("✅ Зимой тратится БОЛЬШЕ денег на проезд")
    elif summer_total > winter_total:
        print("✅ Летом тратится БОЛЬШЕ денег на проезд")
    else:
        print("⚖️ Расходы зимой и летом ОДИНАКОВЫ")
    
    print()
    
    # Находим месяцы с максимальными расходами
    max_expense = np.max(expenses)
    max_months = months[expenses == max_expense]
    
    print("=== МЕСЯЦЫ С НАИБОЛЬШИМИ РАСХОДАМИ ===")
    print(f"Максимальный расход: {max_expense} руб.")
    print(f"Месяцы с максимальными расходами: {list(max_months)}")
    
    # Дополнительная статистика
    print()
    print("=== ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА ===")
    print(f"Средний расход в месяц: {np.mean(expenses):.2f} руб.")
    print(f"Минимальный расход: {np.min(expenses)} руб. (месяц {np.argmin(expenses) + 1})")
    print(f"Общие годовые расходы: {np.sum(expenses)} руб.")
    
    # Визуализация данных
    visualize_expenses(months, expenses, winter_months, summer_months)

def visualize_expenses(months, expenses, winter_months, summer_months):
    """
    Визуализирует расходы по месяцам с выделением зимнего и летнего периодов
    """
    try:
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(12, 6))
        
        # Создаем маски для цветового выделения
        colors = []
        for month in months:
            if month in winter_months:
                colors.append('blue')  # Зимние месяцы - синий
            elif month in summer_months:
                colors.append('red')   # Летние месяцы - красный
            else:
                colors.append('gray')  # Остальные месяцы - серый
        
        # Строим столбчатую диаграмму
        bars = plt.bar(months, expenses, color=colors, alpha=0.7, edgecolor='black')
        
        # Добавляем подписи значений на столбцах
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom')
        
        # Настройка графика
        plt.title('Расходы на проезд по месяцам', fontsize=14, fontweight='bold')
        plt.xlabel('Месяцы', fontsize=12)
        plt.ylabel('Расходы (руб.)', fontsize=12)
        plt.xticks(months, ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 
                           'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'])
        plt.grid(True, alpha=0.3, axis='y')
        
        # Легенда
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='blue', alpha=0.7, label='Зимние месяцы'),
            Patch(facecolor='red', alpha=0.7, label='Летние месяцы'),
            Patch(facecolor='gray', alpha=0.7, label='Остальные месяцы')
        ]
        plt.legend(handles=legend_elements)
        
        plt.tight_layout()
        plt.show()
        
    except ImportError:
        print("Для визуализации установите matplotlib: pip install matplotlib")

# Альтернативная версия с вводом данных пользователем
def analyze_expenses_custom():
    """
    Версия с ручным вводом данных пользователем
    """
    print("\n=== ВВОД ДАННЫХ ===")
    print("Введите расходы на проезд по месяцам (12 чисел через пробел):")
    
    try:
        # Ввод данных
        user_input = input("Расходы: ")
        expenses = np.array([float(x) for x in user_input.split()])
        
        if len(expenses) != 12:
            print("Ошибка: нужно ввести 12 чисел!")
            return
        
        # Вызов основной функции анализа
        analyze_given_expenses(expenses)
        
    except ValueError:
        print("Ошибка: введите числа через пробел!")

def analyze_given_expenses(expenses):
    """
    Анализирует переданный массив расходов
    """
    months = np.arange(1, 13)
    
    # Зимние и летние месяцы
    winter_months = [12, 1, 2]
    winter_indices = [11, 0, 1]
    
    summer_months = [6, 7, 8]
    summer_indices = [5, 6, 7]
    
    # Сравнение периодов
    winter_total = np.sum(expenses[winter_indices])
    summer_total = np.sum(expenses[summer_indices])
    
    print("\n=== РЕЗУЛЬТАТЫ АНАЛИЗА ===")
    print(f"Зимние месяцы {winter_months}: {winter_total:.2f} руб.")
    print(f"Летние месяцы {summer_months}: {summer_total:.2f} руб.")
    
    if winter_total > summer_total:
        print("✅ Зимой тратится БОЛЬШЕ на проезд")
    elif summer_total > winter_total:
        print("✅ Летом тратится БОЛЬШЕ на проезд")
    else:
        print("⚖️ Расходы одинаковы")
    
    # Месяцы с максимальными расходами
    max_expense = np.max(expenses)
    max_months = months[expenses == max_expense]
    
    print(f"\nМаксимальный расход: {max_expense:.2f} руб.")
    print(f"Месяцы с максимальными расходами: {list(max_months)}")

# Дополнительная функция с использованием SciPy для статистики
def advanced_statistics(expenses):
    """
    Расширенная статистика с использованием SciPy
    """
    try:
        from scipy import stats
        
        print("\n=== РАСШИРЕННАЯ СТАТИСТИКА (SciPy) ===")
        print(f"Медиана: {np.median(expenses):.2f} руб.")
        print(f"Стандартное отклонение: {np.std(expenses):.2f} руб.")
        print(f"Коэффициент вариации: {stats.variation(expenses):.2%}")
        
        # Проверка на нормальность (тест Шапиро-Уилка)
        if len(expenses) >= 3 and len(expenses) <= 5000:
            stat, p_value = stats.shapiro(expenses)
            print(f"Тест на нормальность: p-value = {p_value:.4f}")
            if p_value > 0.05:
                print("  Распределение близко к нормальному")
            else:
                print("  Распределение отличается от нормального")
                
    except ImportError:
        print("\nДля расширенной статистики установите scipy: pip install scipy")

# Основная функция
if __name__ == "__main__":
    print("АНАЛИЗ РАСХОДОВ НА ПРОЕЗД ЗА ГОД")
    print("=" * 50)
    
    while True:
        print("\nВыберите вариант:")
        print("1 - Анализ со случайными данными")
        print("2 - Ввод своих данных")
        print("3 - Выход")
        
        choice = input("Ваш выбор (1-3): ").strip()
        
        if choice == '1':
            analyze_transport_expenses()
        elif choice == '2':
            analyze_expenses_custom()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")