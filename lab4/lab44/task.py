import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
from collections import Counter

# Настройка отображения
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Загрузка данных
df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')

# Преобразование дат
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])

print("=== ОБЩИЕ СТАТИСТИКИ ===")
print(f"Всего записей: {len(df)}")
print(f"Период данных: с {df['ISSUE_DATE'].min()} по {df['ISSUE_DATE'].max()}")
print(f"Общая выручка: {df['REVENUE_AMOUNT'].sum():,.0f} руб.")
print(f"Средний чек: {df['REVENUE_AMOUNT'].mean():.0f} руб.")
print(f"Медианный чек: {df['REVENUE_AMOUNT'].median():.0f} руб.")

# 1. Общие описательные статистики
print("\n=== ОПИСАТЕЛЬНЫЕ СТАТИСТИКИ ===")
print(df[['REVENUE_AMOUNT']].describe())

# Визуализация распределения выручки
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.hist(df['REVENUE_AMOUNT'], bins=50, edgecolor='black', alpha=0.7)
plt.title('Распределение суммы продаж')
plt.xlabel('Сумма (руб)')
plt.ylabel('Частота')

# 2. Анализ аэропортов
plt.subplot(2, 3, 2)
top_airports = pd.concat([df['ORIG_CITY_CODE'], df['DEST_CITY_CODE']]).value_counts().head(10)
top_airports.plot(kind='bar')
plt.title('Топ-10 популярных аэропортов')
plt.xticks(rotation=45)

# 3. Анализ сезонности
plt.subplot(2, 3, 3)
monthly_sales = df.groupby(df['ISSUE_DATE'].dt.to_period('M')).size()
monthly_sales.plot(kind='line', marker='o')
plt.title('Динамика продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество продаж')

# 4. Анализ типов пассажиров
plt.subplot(2, 3, 4)
pax_type_counts = df['PAX_TYPE'].value_counts()
plt.pie(pax_type_counts.values, labels=pax_type_counts.index, autopct='%1.1f%%')
plt.title('Распределение по типам пассажиров')

# 5. Анализ способов оплаты
plt.subplot(2, 3, 5)
sale_type_counts = df['SALE_TYPE'].value_counts()
plt.pie(sale_type_counts.values, labels=sale_type_counts.index, autopct='%1.1f%%')
plt.title('Распределение по каналам продаж')

# 6. Анализ программ лояльности
plt.subplot(2, 3, 6)
ffp_counts = df['FFP_FLAG'].value_counts()
ffp_counts = ffp_counts.reindex(['FFP', ''])  # FFP vs не-FFP
ffp_counts.plot(kind='bar')
plt.title('Участие в программе лояльности')
plt.xticks([0, 1], ['FFP', 'Не FFP'], rotation=0)

plt.tight_layout()
plt.show()

# Дополнительный анализ
print("\n=== АНАЛИЗ АЭРОПОРТОВ ===")
print("Самые популярные направления:")
route_counts = df.groupby(['ORIG_CITY_CODE', 'DEST_CITY_CODE']).size().sort_values(ascending=False).head(10)
print(route_counts)

print("\n=== СЕЗОННОСТЬ ===")
# Анализ по дням недели
df['issue_weekday'] = df['ISSUE_DATE'].dt.day_name()
weekday_sales = df.groupby('issue_weekday').size()
print("Продажи по дням недели:")
print(weekday_sales)

# Анализ по месяцам
df['issue_month'] = df['ISSUE_DATE'].dt.month
monthly_revenue = df.groupby('issue_month')['REVENUE_AMOUNT'].sum()
print("\nВыручка по месяцам:")
print(monthly_revenue)

print("\n=== АНАЛИЗ ПАССАЖИРОВ ===")
pax_revenue = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'count', 'sum'])
print("Статистика по типам пассажиров:")
print(pax_revenue)

print("\n=== АНАЛИЗ СПОСОБОВ ОПЛАТЫ ===")
fop_analysis = df['FOP_TYPE_CODE'].value_counts()
print("Распределение способов оплаты:")
print(fop_analysis.head(10))

# Анализ комбинаций способов оплаты
fop_combinations = df['FOP_TYPE_CODE'].str.split(',', expand=True)
fop_single = pd.concat([fop_combinations[0], fop_combinations[1].dropna(), 
                       fop_combinations[2].dropna()]).value_counts()
print("\nПопулярные типы оплаты (включая комбинации):")
print(fop_single.head(10))

# Визуализация дополнительных insights
plt.figure(figsize=(15, 10))

# Сравнение онлайн/оффлайн продаж
plt.subplot(2, 3, 1)
channel_revenue = df.groupby('SALE_TYPE')['REVENUE_AMOUNT'].sum()
plt.pie(channel_revenue.values, labels=channel_revenue.index, autopct='%1.1f%%')
plt.title('Распределение выручки по каналам')

# Средний чек по типам пассажиров
plt.subplot(2, 3, 2)
avg_ticket_by_pax = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].mean()
avg_ticket_by_pax.plot(kind='bar')
plt.title('Средний чек по типам пассажиров')
plt.ylabel('Средняя сумма (руб)')

# Распределение типов перелетов
plt.subplot(2, 3, 3)
flight_type_counts = df['ROUTE_FLIGHT_TYPE'].value_counts()
flight_type_counts.plot(kind='bar')
plt.title('Типы перелетов')
plt.xticks(rotation=45)

# Продажи по программам лояльности
plt.subplot(2, 3, 4)
ffp_revenue = df.groupby('FFP_FLAG')['REVENUE_AMOUNT'].sum()
ffp_revenue = ffp_revenue.reindex(['FFP', ''])
plt.pie(ffp_revenue.values, labels=['FFP', 'Не FFP'], autopct='%1.1f%%')
plt.title('Выручка по программам лояльности')

# Временной анализ - продажи по часам
plt.subplot(2, 3, 5)
df['issue_hour'] = df['ISSUE_DATE'].dt.hour
hourly_sales = df.groupby('issue_hour').size()
hourly_sales.plot(kind='line', marker='o')
plt.title('Продажи по часам суток')
plt.xlabel('Час')
plt.ylabel('Количество продаж')

# Анализ длительности между покупкой и вылетом
plt.subplot(2, 3, 6)
df['days_to_flight'] = (df['FLIGHT_DATE_LOC'] - df['ISSUE_DATE']).dt.days
df['days_to_flight'].hist(bins=30, edgecolor='black', alpha=0.7)
plt.title('Распределение дней до вылета')
plt.xlabel('Дни')
plt.ylabel('Частота')

plt.tight_layout()
plt.show()

# Ключевые выводы
print("\n=== КЛЮЧЕВЫЕ ВЫВОДЫ ===")
print(f"1. Всего обработано {len(df)} транзакций на сумму {df['REVENUE_AMOUNT'].sum():,.0f} руб.")
print(f"2. Средний чек: {df['REVENUE_AMOUNT'].mean():.0f} руб.")
print(f"3. Самые популярные аэропорты: {', '.join(top_airports.head(5).index.tolist())}")
print(f"4. Доля онлайн-продаж: {(df['SALE_TYPE'] == 'ONLINE').mean()*100:.1f}%")
print(f"5. Доля участников FFP: {(df['FFP_FLAG'] == 'FFP').mean()*100:.1f}%")
print(f"6. Среднее время между покупкой и вылетом: {df['days_to_flight'].mean():.1f} дней")

# Прогнозная аналитика (упрощенная)
print("\n=== ПРОГНОЗНАЯ АНАЛИТИКА ===")
# Простой тренд продаж
monthly_trend = df.groupby(df['ISSUE_DATE'].dt.to_period('M')).size()
print("Тренд месячных продаж:")
print(monthly_trend.tail(6))

# Прогноз на основе среднего роста
if len(monthly_trend) > 1:
    growth_rate = monthly_trend.pct_change().mean()
    print(f"\nСреднемесячный темп роста: {growth_rate*100:.2f}%")
    
    # Простой прогноз на следующий месяц
    last_month = monthly_trend.iloc[-1]
    forecast = last_month * (1 + growth_rate)
    print(f"Прогноз продаж на следующий месяц: {forecast:.0f} билетов")