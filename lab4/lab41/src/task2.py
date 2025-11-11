import matplotlib.pyplot as plt
import math

# Создаем списки для данных, избегая точек разрыва
x_left = []    # для x от -10 до -3.001
x_middle = []  # для x от -2.999 до 2.999
x_right = []   # для x от 3.001 до 10

y_left = []
y_middle = []
y_right = []

# Заполняем левую часть (от -10 до -3.001)
x = -10.0
while x <= -3.001:
    x_left.append(x)
    y_left.append(5 / (x**2 - 9))
    x += 0.01  # шаг для плавного графика

# Заполняем среднюю часть (от -2.999 до 2.999)
x = -2.999
while x <= 2.999:
    x_middle.append(x)
    y_middle.append(5 / (x**2 - 9))
    x += 0.01

# Заполняем правую часть (от 3.001 до 10)
x = 3.001
while x <= 10:
    x_right.append(x)
    y_right.append(5 / (x**2 - 9))
    x += 0.01

# Создаем график
plt.figure(figsize=(12, 6))

# Строим три части графика
plt.plot(x_left, y_left, 'b-', linewidth=1.5)
plt.plot(x_middle, y_middle, 'b-', linewidth=1.5)
plt.plot(x_right, y_right, 'b-', linewidth=1.5)

# Добавляем вертикальные асимптоты
plt.axvline(x=-3, color='red', linestyle='--', alpha=0.7, label='Вертикальные асимптоты')
plt.axvline(x=3, color='red', linestyle='--', alpha=0.7)

# Добавляем горизонтальную линию y=0
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)

# Настраиваем внешний вид
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции $f(x) = \\frac{5}{x^2 - 9}$')
plt.grid(True, alpha=0.3)
plt.legend()

# Показываем график
plt.show()