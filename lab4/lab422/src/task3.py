import numpy as np

def solve_linear_system():
    """
    Решение системы линейных уравнений матричным способом
    """
    print("=== РЕШЕНИЕ СИСТЕМЫ ЛИНЕЙНЫХ УРАВНЕНИЙ ===")
    print("Система уравнений:")
    print("-2x₁ - 8.5x₂ - 3.4x₃ + 3.5x₄ = -1.88")
    print("2.4x₂ + 8.2x₄ = -3.28") 
    print("2.5x₁ + 1.6x₂ + 2.1x₃ + 3x₄ = -0.5")
    print("0.3x₁ - 0.4x₂ - 4.8x₃ + 4.6x₄ = -2.83")
    print()
    
    # Формируем матрицу коэффициентов A
    A = np.array([
        [-2, -8.5, -3.4, 3.5],
        [0, 2.4, 0, 8.2],
        [2.5, 1.6, 2.1, 3],
        [0.3, -0.4, -4.8, 4.6]
    ], dtype=float)
    
    print("Матрица коэффициентов A:")
    print(A)
    print()
    
    # Формируем вектор правых частей B
    B = np.array([-1.88, -3.28, -0.5, -2.83], dtype=float)
    
    print("Вектор правых частей B:")
    print(B)
    print()
    
    # Проверяем, является ли матрица A обратимой
    try:
        # Вычисляем определитель матрицы A
        det_A = np.linalg.det(A)
        print(f"Определитель матрицы A: {det_A:.6f}")
        
        if abs(det_A) < 1e-10:
            print("Матрица A вырождена, система не имеет единственного решения")
            return
        
        # Вычисляем обратную матрицу A^(-1)
        A_inv = np.linalg.inv(A)
        
        print("\nОбратная матрица A^(-1):")
        print(A_inv)
        print()
        
        # Вычисляем решение системы: X = A^(-1) * B
        X = np.dot(A_inv, B)
        
        print("Решение системы X = A^(-1) * B:")
        print(f"X = {X}")
        print()
        
        # Округляем значения до одного знака после запятой
        X_rounded = np.round(X, 1)
        
        print("Решение системы (округлено до 1 знака после запятой):")
        print(f"x₁ = {X_rounded[0]}")
        print(f"x₂ = {X_rounded[1]}")
        print(f"x₃ = {X_rounded[2]}")
        print(f"x₄ = {X_rounded[3]}")
        print()
        
        # Проверка решения
        check_solution(A, X, B)
        
        # Альтернативное решение с использованием numpy.linalg.solve
        alternative_solution(A, B)
        
    except np.linalg.LinAlgError:
        print("Ошибка: матрица A вырождена или плохо обусловлена")

def check_solution(A, X, B):
    """
    Проверка корректности решения
    """
    print("=== ПРОВЕРКА РЕШЕНИЯ ===")
    
    # Вычисляем A * X
    calculated_B = np.dot(A, X)
    
    print("Проверка: A * X должно равняться B")
    print(f"Вычисленное A * X: {calculated_B}")
    print(f"Исходный вектор B: {B}")
    print(f"Разность: {calculated_B - B}")
    print(f"Максимальная ошибка: {np.max(np.abs(calculated_B - B)):.10f}")
    
    if np.allclose(calculated_B, B, atol=1e-8):
        print("✅ Решение верное!")
    else:
        print("❌ Решение содержит ошибку!")

def alternative_solution(A, B):
    """
    Альтернативное решение с использованием numpy.linalg.solve
    """
    print("\n=== АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ (numpy.linalg.solve) ===")
    
    try:
        X_solve = np.linalg.solve(A, B)
        X_solve_rounded = np.round(X_solve, 1)
        
        print("Решение с использованием numpy.linalg.solve:")
        print(f"x₁ = {X_solve_rounded[0]}")
        print(f"x₂ = {X_solve_rounded[1]}")
        print(f"x₃ = {X_solve_rounded[2]}")
        print(f"x₄ = {X_solve_rounded[3]}")
        
        # Сравнение методов
        print("\nСравнение методов:")
        print("Оба метода должны давать одинаковый результат")
        
    except np.linalg.LinAlgError:
        print("Ошибка при использовании numpy.linalg.solve")

def detailed_calculation():
    """
    Подробный расчет с промежуточными шагами
    """
    print("\n" + "="*60)
    print("ПОДРОБНЫЙ РАСЧЕТ")
    print("="*60)
    
    A = np.array([
        [-2, -8.5, -3.4, 3.5],
        [0, 2.4, 0, 8.2],
        [2.5, 1.6, 2.1, 3],
        [0.3, -0.4, -4.8, 4.6]
    ], dtype=float)
    
    B = np.array([-1.88, -3.28, -0.5, -2.83], dtype=float)
    
    # Шаг 1: Вычисление определителя
    det_A = np.linalg.det(A)
    print(f"1. Определитель матрицы A: det(A) = {det_A:.6f}")
    
    # Шаг 2: Вычисление обратной матрицы
    A_inv = np.linalg.inv(A)
    print("\n2. Обратная матрица A^(-1):")
    for i, row in enumerate(A_inv):
        print(f"   [{' '.join(f'{x:8.4f}' for x in row)}]")
    
    # Шаг 3: Умножение обратной матрицы на вектор B
    X = np.dot(A_inv, B)
    print(f"\n3. Умножение A^(-1) * B:")
    print(f"   X = A^(-1) * B = {X}")
    
    # Шаг 4: Округление результатов
    X_rounded = np.round(X, 1)
    print(f"\n4. Округление до 1 знака после запятой:")
    print(f"   x₁ = {X[0]:.6f} ≈ {X_rounded[0]}")
    print(f"   x₂ = {X[1]:.6f} ≈ {X_rounded[1]}")
    print(f"   x₃ = {X[2]:.6f} ≈ {X_rounded[2]}")
    print(f"   x₄ = {X[3]:.6f} ≈ {X_rounded[3]}")

# Основная программа
if __name__ == "__main__":
    print("РЕШЕНИЕ СИСТЕМЫ ЛИНЕЙНЫХ УРАВНЕНИЙ МАТРИЧНЫМ СПОСОБОМ")
    print("=" * 70)
    
    while True:
        print("\nВыберите вариант:")
        print("1 - Основное решение")
        print("2 - Подробный расчет с шагами")
        print("3 - Выход")
        
        choice = input("Ваш выбор (1-3): ").strip()
        
        if choice == '1':
            solve_linear_system()
        elif choice == '2':
            detailed_calculation()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")