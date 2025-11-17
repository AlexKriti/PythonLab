import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, Polygon
import threading
import os

    

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 8))

# Тело бобра (основной овал)
body = Ellipse((0, 0), width=6, height=3, facecolor='#8B4513', edgecolor='black', linewidth=2)
ax.add_patch(body)

# Голова
head = Ellipse((3, 0.5), width=2.5, height=2, facecolor='#8B4513', edgecolor='black', linewidth=2)
ax.add_patch(head)

# Нос
nose = Circle((4, 0.5), radius=0.1, facecolor='black')
ax.add_patch(nose)

# Глазa
eye1 = Circle((3.8, 1), radius=0.2, facecolor='black')
eye2 = Circle((3.3, 1), radius=0.2, facecolor='black')
eye_in1 = Circle((3.8, 1), radius=0.1, facecolor='white')
eye_in2 = Circle((3.3, 1), radius=0.1, facecolor='white')
eye_in11 = Circle((3.82, 1), radius=0.05, facecolor='black')
eye_in12 = Circle((3.32, 1), radius=0.05, facecolor='black')
ax.add_patch(eye1)
ax.add_patch(eye2)
ax.add_patch(eye_in1)
ax.add_patch(eye_in2)
ax.add_patch(eye_in11)
ax.add_patch(eye_in12)


# Уши - подняты выше и касаются головы
ear_left = Ellipse((2.8, 1.6), width=0.6, height=0.4, facecolor='#8B4513', edgecolor='black')
ear_right = Ellipse((3.5, 1.6), width=0.6, height=0.4, facecolor='#8B4513', edgecolor='black')
ax.add_patch(ear_left)
ax.add_patch(ear_right)

# Точки внутри ушей
ear_dot_left = Circle((2.8, 1.6), radius=0.1, facecolor='#654321')
ear_dot_right = Circle((3.5, 1.6), radius=0.1, facecolor='#654321')
ax.add_patch(ear_dot_left)
ax.add_patch(ear_dot_right)

# Хвост (плоский хвост бобра)
tail_points = [(-3.5, -0.2), (-4.5, 0.3), (-3.5, 0.8), (-2.5, 0.3)]
# tail = Polygon(tail_points, facecolor='#654321', edgecolor='black')
tail = Ellipse((-3.5, -0.2), width=1.6, height=0.8, facecolor='#654321', edgecolor='black')
ax.add_patch(tail)

# Передние лапы (только левая)
front_leg_left = Ellipse((1.5, -1.2), width=0.8, height=1.2, facecolor='#8B4513', edgecolor='black')
ax.add_patch(front_leg_left)

# Задние лапы (обе)
back_leg_left = Ellipse((-1.5, -1.2), width=0.8, height=1.2, facecolor='#8B4513', edgecolor='black')
back_leg_right = Ellipse((-2.2, -1.2), width=0.8, height=1.2, facecolor='#8B4513', edgecolor='black')
ax.add_patch(back_leg_left)
ax.add_patch(back_leg_right)

# Зубы (смещены к центру мордочки)
tooth_left = Rectangle((3.5, -0.2), width=0.15, height=0.4, facecolor='white', edgecolor='black')
tooth_right = Rectangle((3.7, -0.2), width=0.15, height=0.4, facecolor='white', edgecolor='black')
ax.add_patch(tooth_left)
ax.add_patch(tooth_right)

# Бревно (бобер держит бревно)
log_points = [(-1, 0.6), (1, 1.8), (2, 1.2), (0, 0)]
log = Polygon(log_points, facecolor='#D2B48C', edgecolor='#8B4513', linewidth=2)
ax.add_patch(log)

# Лапы на бревне (только одна)
paw_on_log = Ellipse((0.5, 1.8), width=0.6, height=0.4, facecolor='#8B4513', edgecolor='black')
ax.add_patch(paw_on_log)

# Настраиваем отображение
ax.set_xlim(-5, 6)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
ax.axis('off')  # Убираем оси


plt.tight_layout()
plt.show()