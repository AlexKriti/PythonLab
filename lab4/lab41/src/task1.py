import matplotlib.pyplot as plt
import math

# Создаем списки для данных
x_degrees = []
f_x_values = []
h_x_values = []

# Заполняем данные с шагом 1 градус
for degrees in range(-360, 361):
    x_degrees.append(degrees)
    
    # Переводим градусы в радианы
    radians = math.radians(degrees)
    radians_06x = math.radians(degrees * 0.6)
    
    # Вычисляем первую функцию f(x)
    cos_x = math.cos(radians)
    cos_06x = math.cos(radians_06x)
    sin_x = math.sin(radians)
    
    term1 = math.exp(cos_x)
    term2 = math.log(cos_06x**2 + 1) * sin_x
    f_x = term1 + term2
    
    # Вычисляем вторую функцию h(x)
    cos_plus_sin = cos_x + sin_x
    h_x = -math.log(cos_plus_sin**2 + 2.5) + 10
    
    f_x_values.append(f_x)
    h_x_values.append(h_x)

# Создаем график
plt.figure(figsize=(14, 8))

# Строим графики обеих функций
plt.plot(x_degrees, f_x_values, 'b-', linewidth=2, label='$f(x) = e^{cosx} + ln(cos^2(0.6x) + 1) cdot sinx$')
plt.plot(x_degrees, h_x_values, 'r-', linewidth=2, label='$h(x) = -ln((cosx + sinx)^2 + 2.5) + 10$')

# Настраиваем внешний вид графика
plt.xlabel('Градусы (°)', fontsize=12)
plt.ylabel('f(x), h(x)', fontsize=12)
plt.title('Графики функций f(x) и h(x) на интервале [-360°, 360°]', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# Настраиваем ось X для отображения градусов
plt.xlim(-360, 360)
plt.xticks(range(-360, 361, 90))  # Метки каждые 90 градусов

# Добавляем горизонтальную линию y=0 для лучшей читаемости
plt.axhline(y=0, color='k', linestyle='-', alpha=0.2)

# Показываем график
plt.tight_layout()
plt.show()