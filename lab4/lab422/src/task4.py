import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def definite_integral_examples():
    """
    Вычисление определенных интегралов различными методами
    """
    print("=== ВЫЧИСЛЕНИЕ ОПРЕДЕЛЕННЫХ ИНТЕГРАЛОВ ===")
    
    # Пример 1: ∫sin(x) dx от 0 до π
    def f1(x):
        return np.sin(x)
    
    a1, b1 = 0, np.pi
    exact1 = 2.0  # Точное значение
    
    # Вычисление различными методами
    result_quad, error_quad = integrate.quad(f1, a1, b1)
    result_trapz = integrate.trapz(f1(np.linspace(a1, b1, 1000)), np.linspace(a1, b1, 1000))
    result_simps = integrate.simps(f1(np.linspace(a1, b1, 1000)), np.linspace(a1, b1, 1000))
    
    print(f"\n1. ∫sin(x) dx от 0 до π")
    print(f"   Точное значение: {exact1}")
    print(f"   scipy.integrate.quad: {result_quad:.6f} (ошибка: {error_quad:.2e})")
    print(f"   scipy.integrate.trapz: {result_trapz:.6f}")
    print(f"   scipy.integrate.simps: {result_simps:.6f}")
    
    # Визуализация
    visualize_definite_integral(f1, a1, b1, "sin(x)", exact1)
    
    # Пример 2: ∫x² dx от 0 до 2
    def f2(x):
        return x**2
    
    a2, b2 = 0, 2
    exact2 = 8/3  # Точное значение
    
    result_quad2, error_quad2 = integrate.quad(f2, a2, b2)
    
    print(f"\n2. ∫x² dx от 0 до 2")
    print(f"   Точное значение: {exact2:.6f}")
    print(f"   scipy.integrate.quad: {result_quad2:.6f} (ошибка: {error_quad2:.2e})")
    
    # Пример 3: ∫e^(-x²) dx от 0 до ∞ (интеграл Гаусса)
    def f3(x):
        return np.exp(-x**2)
    
    result_quad3, error_quad3 = integrate.quad(f3, 0, np.inf)
    exact3 = np.sqrt(np.pi)/2
    
    print(f"\n3. ∫e^(-x²) dx от 0 до ∞ (интеграл Гаусса)")
    print(f"   Точное значение: {exact3:.6f}")
    print(f"   scipy.integrate.quad: {result_quad3:.6f} (ошибка: {error_quad3:.2e})")

def double_integral_examples():
    """
    Вычисление двойных интегралов
    """
    print("\n" + "="*50)
    print("=== ВЫЧИСЛЕНИЕ ДВОЙНЫХ ИНТЕГРАЛОВ ===")
    
    # Пример 1: ∫∫(x*y) dxdy по области [0,1]×[0,1]
    def f1(x, y):
        return x * y
    
    # Пределы интегрирования
    x1_min, x1_max = 0, 1
    y1_min, y1_max = 0, 1
    exact1 = 0.25  # Точное значение
    
    result_dblquad1, error_dblquad1 = integrate.dblquad(f1, x1_min, x1_max, 
                                                      lambda x: y1_min, lambda x: y1_max)
    
    print(f"\n1. ∫∫(x*y) dxdy по области [0,1]×[0,1]")
    print(f"   Точное значение: {exact1}")
    print(f"   scipy.integrate.dblquad: {result_dblquad1:.6f} (ошибка: {error_dblquad1:.2e})")
    
    # Визуализация
    visualize_double_integral(f1, x1_min, x1_max, y1_min, y1_max, "x*y")
    
    # Пример 2: ∫∫sin(x+y) dxdy по области [0,π]×[0,π]
    def f2(x, y):
        return np.sin(x + y)
    
    x2_min, x2_max = 0, np.pi
    y2_min, y2_max = 0, np.pi
    exact2 = 0.0  # Точное значение
    
    result_dblquad2, error_dblquad2 = integrate.dblquad(f2, x2_min, x2_max,
                                                      lambda x: y2_min, lambda x: y2_max)
    
    print(f"\n2. ∫∫sin(x+y) dxdy по области [0,π]×[0,π]")
    print(f"   Точное значение: {exact2}")
    print(f"   scipy.integrate.dblquad: {result_dblquad2:.6f} (ошибка: {error_dblquad2:.2e})")
    
    # Пример 3: ∫∫e^(-x²-y²) dxdy по всей плоскости (интеграл Гаусса)
    def f3(x, y):
        return np.exp(-x**2 - y**2)
    
    result_dblquad3, error_dblquad3 = integrate.dblquad(f3, -np.inf, np.inf,
                                                      lambda x: -np.inf, lambda x: np.inf)
    exact3 = np.pi  # Точное значение
    
    print(f"\n3. ∫∫e^(-x²-y²) dxdy по всей плоскости")
    print(f"   Точное значение: {exact3:.6f}")
    print(f"   scipy.integrate.dblquad: {result_dblquad3:.6f} (ошибка: {error_dblquad3:.2e})")

def monte_carlo_integration():
    """
    Вычисление интегралов методом Монте-Карло
    """
    print("\n" + "="*50)
    print("=== МЕТОД МОНТЕ-КАРЛО ===")
    
    # Одномерный интеграл ∫sin(x) dx от 0 до π
    def f1(x):
        return np.sin(x)
    
    a1, b1 = 0, np.pi
    exact1 = 2.0
    
    # Генерируем случайные точки
    n_points = 100000
    x_random = np.random.uniform(a1, b1, n_points)
    y_values = f1(x_random)
    
    # Оценка интеграла
    mc_result1 = (b1 - a1) * np.mean(y_values)
    
    print(f"\nМонте-Карло: ∫sin(x) dx от 0 до π")
    print(f"   Точное значение: {exact1}")
    print(f"   Монте-Карло оценка: {mc_result1:.6f}")
    print(f"   Относительная ошибка: {abs(mc_result1 - exact1)/exact1*100:.4f}%")
    
    # Двумерный интеграл ∫∫(x*y) dxdy по области [0,1]×[0,1]
    def f2(x, y):
        return x * y
    
    n_points_2d = 100000
    x_random = np.random.uniform(0, 1, n_points_2d)
    y_random = np.random.uniform(0, 1, n_points_2d)
    z_values = f2(x_random, y_random)
    
    mc_result2 = np.mean(z_values)  # Площадь области = 1
    
    print(f"\nМонте-Карло: ∫∫(x*y) dxdy по области [0,1]×[0,1]")
    print(f"   Точное значение: 0.25")
    print(f"   Монте-Карло оценка: {mc_result2:.6f}")
    print(f"   Относительная ошибка: {abs(mc_result2 - 0.25)/0.25*100:.4f}%")

def visualize_definite_integral(f, a, b, func_name, exact_value):
    """
    Визуализация определенного интеграла
    """
    try:
        x = np.linspace(a - 0.5, b + 0.5, 1000)
        y = f(x)
        
        # Область под кривой
        x_fill = np.linspace(a, b, 100)
        y_fill = f(x_fill)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {func_name}')
        plt.fill_between(x_fill, y_fill, alpha=0.3, color='red', 
                        label=f'∫f(x)dx ≈ {exact_value:.3f}')
        
        plt.axvline(a, color='gray', linestyle='--', alpha=0.7)
        plt.axvline(b, color='gray', linestyle='--', alpha=0.7)
        plt.axhline(0, color='black', linewidth=0.5)
        
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Определенный интеграл ∫{func_name}dx от {a} до {b}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except Exception as e:
        print(f"Ошибка при визуализации: {e}")

def visualize_double_integral(f, x_min, x_max, y_min, y_max, func_name):
    """
    Визуализация двойного интеграла
    """
    try:
        # Создаем сетку для 3D графика
        x = np.linspace(x_min, x_max, 50)
        y = np.linspace(y_min, y_max, 50)
        X, Y = np.meshgrid(x, y)
        Z = f(X, Y)
        
        fig = plt.figure(figsize=(12, 5))
        
        # 3D поверхность
        ax1 = fig.add_subplot(121, projection='3d')
        surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('f(X,Y)')
        ax1.set_title(f'f(x,y) = {func_name}')
        
        # 2D контурный график
        ax2 = fig.add_subplot(122)
        contour = ax2.contourf(X, Y, Z, levels=20, cmap='viridis')
        plt.colorbar(contour, ax=ax2)
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_title(f'Контурный график f(x,y) = {func_name}')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Ошибка при визуализации: {e}")

def custom_integral_calculator():
    """
    Калькулятор для вычисления пользовательских интегралов
    """
    print("\n" + "="*50)
    print("=== КАЛЬКУЛЯТОР ИНТЕГРАЛОВ ===")
    
    while True:
        print("\nВыберите тип интеграла:")
        print("1 - Определенный интеграл")
        print("2 - Двойной интеграл")
        print("3 - Вернуться в главное меню")
        
        choice = input("Ваш выбор (1-3): ").strip()
        
        if choice == '1':
            calculate_custom_single()
        elif choice == '2':
            calculate_custom_double()
        elif choice == '3':
            break
        else:
            print("Неверный выбор!")

def calculate_custom_single():
    """
    Вычисление пользовательского определенного интеграла
    """
    try:
        print("\n--- Пользовательский определенный интеграл ---")
        func_str = input("Введите функцию f(x) (используйте x как переменную): ")
        a = float(input("Нижний предел a: "))
        b = float(input("Верхний предел b: "))
        
        # Создаем функцию из строки
        def f(x):
            return eval(func_str)
        
        # Вычисляем интеграл
        result, error = integrate.quad(f, a, b)
        
        print(f"\nРезультат: ∫({func_str}) dx от {a} до {b}")
        print(f"Значение: {result:.8f}")
        print(f"Погрешность: {error:.2e}")
        
        # Визуализация
        visualize_definite_integral(f, a, b, func_str, result)
        
    except Exception as e:
        print(f"Ошибка: {e}")

def calculate_custom_double():
    """
    Вычисление пользовательского двойного интеграла
    """
    try:
        print("\n--- Пользовательский двойной интеграл ---")
        func_str = input("Введите функцию f(x,y) (используйте x и y как переменные): ")
        x_min = float(input("Нижний предел по x: "))
        x_max = float(input("Верхний предел по x: "))
        y_min = float(input("Нижний предел по y: "))
        y_max = float(input("Верхний предел по y: "))
        
        # Создаем функцию из строки
        def f(x, y):
            return eval(func_str)
        
        # Вычисляем интеграл
        result, error = integrate.dblquad(f, x_min, x_max, 
                                        lambda x: y_min, lambda x: y_max)
        
        print(f"\nРезультат: ∫∫({func_str}) dxdy")
        print(f"Область: x∈[{x_min}, {x_max}], y∈[{y_min}, {y_max}]")
        print(f"Значение: {result:.8f}")
        print(f"Погрешность: {error:.2e}")
        
        # Визуализация
        visualize_double_integral(f, x_min, x_max, y_min, y_max, func_str)
        
    except Exception as e:
        print(f"Ошибка: {e}")

# Основная программа
if __name__ == "__main__":
    print("ВЫЧИСЛЕНИЕ ОПРЕДЕЛЕННЫХ И ДВОЙНЫХ ИНТЕГРАЛОВ")
    print("=" * 60)
    
    while True:
        print("\nГлавное меню:")
        print("1 - Примеры определенных интегралов")
        print("2 - Примеры двойных интегралов")
        print("3 - Метод Монте-Карло")
        print("4 - Калькулятор интегралов")
        print("5 - Выход")
        
        choice = input("Ваш выбор (1-5): ").strip()
        
        if choice == '1':
            definite_integral_examples()
        elif choice == '2':
            double_integral_examples()
        elif choice == '3':
            monte_carlo_integration()
        elif choice == '4':
            custom_integral_calculator()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")