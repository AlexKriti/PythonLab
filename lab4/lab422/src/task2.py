import numpy as np

def calculate_journey():
    """
    Решает задачу расчета пути, времени и средней скорости автомобиля
    на участках дороги с k по p
    """
    print("=== РАСЧЕТ ПАРАМЕТРОВ ДВИЖЕНИЯ АВТОМОБИЛЯ ===")
    
    # Входные данные из теста
    lengths_str = "20 8 9 18 5 12 16 16 6 7"
    speeds_str = "44 70 44 66 46 38 38 37 66 67"
    k = 4
    p = 7
    
    print("Входные данные:")
    print(f"Длины участков: {lengths_str}")
    print(f"Скорости на участках: {speeds_str}")
    print(f"Начальный участок (k): {k}")
    print(f"Конечный участок (p): {p}")
    print()
    
    # Преобразуем строки в массивы NumPy
    lengths = np.array([float(x) for x in lengths_str.split()])
    speeds = np.array([float(x) for x in speeds_str.split()])
    
    # Проверка корректности данных
    if len(lengths) != len(speeds):
        print("Ошибка: количество участков длин и скоростей не совпадает!")
        return
    
    if k < 1 or p > len(lengths) or k > p:
        print("Ошибка: некорректные значения k и p!")
        return
    
    # Нумерация участков с 1, индексы с 0
    start_idx = k - 1  # индекс начального участка
    end_idx = p - 1    # индекс конечного участка
    
    # Выбираем нужные участки
    selected_lengths = lengths[start_idx:end_idx + 1]
    selected_speeds = speeds[start_idx:end_idx + 1]
    
    print(f"Участки с {k} по {p}:")
    for i, (length, speed) in enumerate(zip(selected_lengths, selected_speeds), k):
        print(f"  Участок {i}: длина = {length} км, скорость = {speed} км/ч")
    print()
    
    # Расчет параметров
    total_distance = np.sum(selected_lengths)  # общий путь
    
    # Время на каждом участке = расстояние / скорость
    times = selected_lengths / selected_speeds
    total_time = np.sum(times)  # общее время
    
    # Средняя скорость = общий путь / общее время
    average_speed = total_distance / total_time
    
    print("=== РЕЗУЛЬТАТЫ ===")
    print(f"Общий путь (S): {total_distance:.2f} км")
    print(f"Общее время (T): {total_time:.2f} час")
    print(f"Средняя скорость (V): {average_speed:.2f} км/ч")
    
    # Сравнение с тестовыми данными
    print("\n=== СРАВНЕНИЕ С ТЕСТОМ ===")
    print(f"Тестовые значения: S = 49 км, T = 1.28 час, V = 38.34 км/ч")
    print(f"Наши значения:     S = {total_distance:.0f} км, T = {total_time:.2f} час, V = {average_speed:.2f} км/ч")
    
    # Визуализация
    visualize_results(selected_lengths, selected_speeds, times, k, p)

def visualize_results(lengths, speeds, times, k, p):
    """
    Визуализирует результаты расчета
    """
    try:
        import matplotlib.pyplot as plt
        
        # Создаем график с тремя подграфиками
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        
        # График 1: Длины участков
        segments = np.arange(k, p + 1)
        bars1 = ax1.bar(segments, lengths, color='skyblue', alpha=0.7, edgecolor='navy')
        ax1.set_title('Длины участков дороги')
        ax1.set_xlabel('Номер участка')
        ax1.set_ylabel('Длина (км)')
        ax1.grid(True, alpha=0.3)
        
        # Добавляем значения на столбцы
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}', ha='center', va='bottom')
        
        # График 2: Скорости на участках
        bars2 = ax2.bar(segments, speeds, color='lightcoral', alpha=0.7, edgecolor='darkred')
        ax2.set_title('Скорости на участках')
        ax2.set_xlabel('Номер участка')
        ax2.set_ylabel('Скорость (км/ч)')
        ax2.grid(True, alpha=0.3)
        
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}', ha='center', va='bottom')
        
        # График 3: Время на участках
        bars3 = ax3.bar(segments, times, color='lightgreen', alpha=0.7, edgecolor='darkgreen')
        ax3.set_title('Время прохождения участков')
        ax3.set_xlabel('Номер участка')
        ax3.set_ylabel('Время (час)')
        ax3.grid(True, alpha=0.3)
        
        for bar in bars3:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
        
    except ImportError:
        print("\nДля визуализации установите matplotlib: pip install matplotlib")

def calculate_with_user_input():
    """
    Версия с вводом данных пользователем
    """
    print("\n=== ВВОД ДАННЫХ ПОЛЬЗОВАТЕЛЕМ ===")
    
    try:
        # Ввод длин участков
        lengths_str = input("Введите длины участков через пробел: ")
        lengths = np.array([float(x) for x in lengths_str.split()])
        
        # Ввод скоростей
        speeds_str = input("Введите скорости на участках через пробел: ")
        speeds = np.array([float(x) for x in speeds_str.split()])
        
        # Проверка совпадения количества
        if len(lengths) != len(speeds):
            print("Ошибка: количество участков длин и скоростей должно совпадать!")
            return
        
        # Ввод k и p
        k = int(input("Введите номер начального участка (k): "))
        p = int(input("Введите номер конечного участка (p): "))
        
        # Проверка корректности k и p
        if k < 1 or p > len(lengths) or k > p:
            print("Ошибка: некорректные значения k и p!")
            return
        
        # Расчет
        start_idx = k - 1
        end_idx = p - 1
        
        selected_lengths = lengths[start_idx:end_idx + 1]
        selected_speeds = speeds[start_idx:end_idx + 1]
        
        total_distance = np.sum(selected_lengths)
        times = selected_lengths / selected_speeds
        total_time = np.sum(times)
        average_speed = total_distance / total_time
        
        print("\n=== РЕЗУЛЬТАТЫ ===")
        print(f"Участки с {k} по {p}:")
        for i, (length, speed) in enumerate(zip(selected_lengths, selected_speeds), k):
            print(f"  Участок {i}: длина = {length} км, скорость = {speed} км/ч")
        
        print(f"\nОбщий путь (S): {total_distance:.2f} км")
        print(f"Общее время (T): {total_time:.2f} час")
        print(f"Средняя скорость (V): {average_speed:.2f} км/ч")
        
    except ValueError:
        print("Ошибка ввода данных! Убедитесь, что вводите числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def advanced_calculation():
    """
    Расширенная версия с дополнительной статистикой
    """
    print("\n=== РАСШИРЕННЫЙ РАСЧЕТ ===")
    
    # Данные из теста
    lengths = np.array([20, 8, 9, 18, 5, 12, 16, 16, 6, 7])
    speeds = np.array([44, 70, 44, 66, 46, 38, 38, 37, 66, 67])
    k, p = 4, 7
    
    selected_lengths = lengths[k-1:p]
    selected_speeds = speeds[k-1:p]
    
    # Основные расчеты
    total_distance = np.sum(selected_lengths)
    times = selected_lengths / selected_speeds
    total_time = np.sum(times)
    average_speed = total_distance / total_time
    
    # Дополнительная статистика
    print("Дополнительная статистика:")
    print(f"Количество участков: {len(selected_lengths)}")
    print(f"Самый длинный участок: {np.max(selected_lengths)} км (участок {np.argmax(selected_lengths) + k})")
    print(f"Самый короткий участок: {np.min(selected_lengths)} км (участок {np.argmin(selected_lengths) + k})")
    print(f"Максимальная скорость: {np.max(selected_speeds)} км/ч")
    print(f"Минимальная скорость: {np.min(selected_speeds)} км/ч")
    print(f"Самый быстрый участок по времени: {np.min(times):.3f} час")
    print(f"Самый медленный участок по времени: {np.max(times):.3f} час")
    
    # Взвешенная средняя скорость
    weighted_avg_speed = np.average(selected_speeds, weights=selected_lengths)
    print(f"Взвешенная средняя скорость: {weighted_avg_speed:.2f} км/ч")

# Основная программа
if __name__ == "__main__":
    print("РАСЧЕТ ПАРАМЕТРОВ ДВИЖЕНИЯ АВТОМОБИЛЯ")
    print("=" * 50)
    
    while True:
        print("\nВыберите вариант:")
        print("1 - Расчет с тестовыми данными")
        print("2 - Ввод своих данных")
        print("3 - Расширенная статистика")
        print("4 - Выход")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == '1':
            calculate_journey()
        elif choice == '2':
            calculate_with_user_input()
        elif choice == '3':
            advanced_calculation()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")
            
# 15 23 26 71 45 29 61
# 19 33 46 51 85 19 71