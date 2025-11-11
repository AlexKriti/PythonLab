import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

print("Загрузка данных...")

# Загрузка данных
try:
    df = pd.read_excel('lab_4_part_5.xlsx', sheet_name='Данные', header=2)
    print("Данные успешно загружены")
except Exception as e:
    print(f"Ошибка загрузки: {e}")
    exit()

# Базовая предобработка
print(f"Размер данных: {df.shape}")
print("Столбцы:", df.columns.tolist())

# ДИАГНОСТИКА: посмотрим на реальные данные
print("\nДИАГНОСТИКА ДАННЫХ:")
print("Первые 3 строки данных:")
for i in range(min(3, len(df))):
    print(f"Строка {i}: {df.iloc[i].tolist()}")

print("\nТипы данных до преобразования:")
print(df.dtypes)

# ПЕРЕИМЕНОВАНИЕ СТОЛБЦОВ - корректно для 10 столбцов
new_columns = [
    'ID', 'Дата', 'Год', 'Месяц_год', 'Местоположение', 
    'Бренд', 'Товар', 'Количество', 'Продажи', 'Себестоимость'
]
df.columns = new_columns
print("Столбцы переименованы")

# ПРЕОБРАЗОВАНИЕ ТИПОВ - БЕЗ УДАЛЕНИЯ ДАННЫХ
# Сначала сохраним исходные данные для диагностики
print("\nДанные столбца 'Количество' до преобразования:")
print(df['Количество'].head())
print("Уникальные значения:", df['Количество'].unique()[:10])

print("\nДанные столбца 'Продажи' до преобразования:")
print(df['Продажи'].head())
print("Уникальные значения:", df['Продажи'].unique()[:10])

print("\nДанные столбца 'Себестоимость' до преобразования:")
print(df['Себестоимость'].head())
print("Уникальные значения:", df['Себестоимость'].unique()[:10])

# Преобразование типов с сохранением исходных значений при ошибке
df['Дата'] = pd.to_datetime(df['Дата'], errors='coerce')

# Для числовых столбцов - попробуем разные стратегии
def safe_convert_to_numeric(series):
    """Безопасное преобразование в числовой формат"""
    # Пробуем преобразовать как есть
    result = pd.to_numeric(series, errors='coerce')
    
    # Если много NaN, пробуем альтернативные подходы
    if result.isna().sum() > len(result) * 0.5:
        print(f"Много NaN в столбце {series.name}, пробуем альтернативные методы...")
        
        # Пробуем убрать пробелы и нечисловые символы
        cleaned = series.astype(str).str.replace(r'[^\d.-]', '', regex=True)
        result = pd.to_numeric(cleaned, errors='coerce')
    
    return result

# Применяем безопасное преобразование
df['Количество'] = safe_convert_to_numeric(df['Количество'])
df['Продажи'] = safe_convert_to_numeric(df['Продажи'])
df['Себестоимость'] = safe_convert_to_numeric(df['Себестоимость'])

print(f"\nПосле преобразования - NaN значений:")
print(f"Количество: {df['Количество'].isna().sum()}")
print(f"Продажи: {df['Продажи'].isna().sum()}")
print(f"Себестоимость: {df['Себестоимость'].isna().sum()}")

# ЗАПОЛНЕНИЕ NaN вместо удаления
initial_count = len(df)

# Заполняем числовые столбцы нулями вместо удаления
df['Количество'] = df['Количество'].fillna(0)
df['Продажи'] = df['Продажи'].fillna(0) 
df['Себестоимость'] = df['Себестоимость'].fillna(0)

# Удаляем только строки, где ВСЕ ключевые столбцы пустые
key_columns = ['Количество', 'Продажи', 'Себестоимость']
df = df[~(df[key_columns] == 0).all(axis=1)]

print(f"Сохранили {len(df)} из {initial_count} строк")

# Базовые расчеты (только для ненулевых значений)
mask = (df['Продажи'] > 0) & (df['Себестоимость'] > 0)
df['Прибыль'] = 0
df['Рентабельность'] = 0

df.loc[mask, 'Прибыль'] = df.loc[mask, 'Продажи'] - df.loc[mask, 'Себестоимость']
df.loc[mask, 'Рентабельность'] = (df.loc[mask, 'Прибыль'] / df.loc[mask, 'Себестоимость'] * 100).round(2)

print(f"\nОбработано записей: {len(df)}")
if len(df) > 0:
    print(f"Период: {df['Дата'].min()} - {df['Дата'].max()}")
    print(f"Уникальные товары: {df['Товар'].nunique()}")
    print(f"Уникальные бренды: {df['Бренд'].nunique()}")
else:
    print("НЕТ ДАННЫХ ДЛЯ АНАЛИЗА!")
    exit()

# АНАЛИЗ И ВИЗУАЛИЗАЦИЯ
print("\nСоздание отчетов...")

# 1. Основные метрики (только ненулевые данные)
valid_data = df[(df['Продажи'] > 0) & (df['Себестоимость'] > 0)]

if len(valid_data) > 0:
    total_sales = valid_data['Продажи'].sum()
    total_cost = valid_data['Себестоимость'].sum()
    total_profit = valid_data['Прибыль'].sum()
    avg_profitability = (total_profit / total_cost * 100).round(2)
else:
    total_sales = total_cost = total_profit = avg_profitability = 0

print("="*50)
print("ОСНОВНЫЕ ПОКАЗАТЕЛИ")
print("="*50)
print(f"Общий объем продаж: {total_sales:,.0f} руб.")
print(f"Общая себестоимость: {total_cost:,.0f} руб.")
print(f"Общая прибыль: {total_profit:,.0f} руб.")
print(f"Средняя рентабельность: {avg_profitability}%")

# 2. Анализ по брендам (только с данными)
if len(df[df['Продажи'] > 0]) > 0:
    brand_summary = df[df['Продажи'] > 0].groupby('Бренд').agg({
        'Продажи': 'sum',
        'Прибыль': 'sum',
        'Количество': 'sum'
    }).round(2)
    
    if total_sales > 0:
        brand_summary['Доля_рынка'] = (brand_summary['Продажи'] / total_sales * 100).round(2)
    
    print("\n" + "="*50)
    print("АНАЛИЗ ПО БРЕНДАМ")
    print("="*50)
    print(brand_summary.sort_values('Продажи', ascending=False))
else:
    brand_summary = pd.DataFrame()
    print("Нет данных для анализа по брендам")

# 3. Анализ по товарам (только с данными)
if len(df[df['Продажи'] > 0]) > 0:
    product_summary = df[df['Продажи'] > 0].groupby('Товар').agg({
        'Продажи': 'sum',
        'Прибыль': 'sum',
        'Количество': 'sum'
    }).round(2)
    
    print("\n" + "="*50)
    print("ТОП-10 ТОВАРОВ ПО ПРИБЫЛИ")
    print("="*50)
    if len(product_summary) > 0:
        print(product_summary.nlargest(min(10, len(product_summary)), 'Прибыль')[['Продажи', 'Прибыль']])
    else:
        print("Нет данных о товарах")
else:
    product_summary = pd.DataFrame()
    print("Нет данных для анализа по товарам")

# ВИЗУАЛИЗАЦИИ (только если есть данные)
try:
    if len(df[df['Продажи'] > 0]) > 0:
        # 1. Продажи по брендам
        plt.figure(figsize=(10, 6))
        brand_sales = df[df['Продажи'] > 0].groupby('Бренд')['Продажи'].sum().sort_values(ascending=False)
        if len(brand_sales) > 0:
            plt.bar(brand_sales.index, brand_sales.values)
            plt.title('Продажи по брендам')
            plt.ylabel('Продажи (руб)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('brand_sales.png')
            plt.close()
            print("✓ График 'Продажи по брендам' сохранен как brand_sales.png")
        
        # 2. Динамика продаж по месяцам
        plt.figure(figsize=(12, 6))
        monthly_data = df[df['Продажи'] > 0].copy()
        if len(monthly_data) > 0:
            monthly_data['Месяц'] = monthly_data['Дата'].dt.to_period('M')
            monthly_sales = monthly_data.groupby('Месяц')['Продажи'].sum()
            if len(monthly_sales) > 0:
                plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
                plt.title('Динамика продаж по месяцам')
                plt.ylabel('Продажи (руб)')
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()
                plt.savefig('monthly_sales.png')
                plt.close()
                print("✓ График 'Динамика продаж' сохранен как monthly_sales.png")
        
        # 3. Топ товаров по прибыли
        plt.figure(figsize=(10, 6))
        if len(product_summary) > 0:
            top_products = product_summary.nlargest(min(10, len(product_summary)), 'Прибыль')['Прибыль']
            plt.barh(top_products.index, top_products.values)
            plt.title('Топ товаров по прибыли')
            plt.xlabel('Прибыль (руб)')
            plt.tight_layout()
            plt.savefig('top_products.png')
            plt.close()
            print("✓ График 'Топ товаров' сохранен как top_products.png")
    
except Exception as e:
    print(f"Ошибка при создании графиков: {e}")

# СОХРАНЕНИЕ ОТЧЕТОВ
try:
    # Сохраняем обработанные данные
    df.to_csv('processed_data.csv', encoding='utf-8-sig', index=False)
    print("✓ Обработанные данные сохранены как processed_data.csv")
    
    if len(product_summary) > 0:
        product_summary.to_csv('sales_analysis_report.csv', encoding='utf-8-sig')
        print("✓ Отчет по товарам сохранен как sales_analysis_report.csv")
    
    if len(brand_summary) > 0:
        brand_summary.to_csv('brand_analysis_report.csv', encoding='utf-8-sig')
        print("✓ Отчет по брендам сохранен как brand_analysis_report.csv")
        
except Exception as e:
    print(f"Ошибка при сохранении отчетов: {e}")

print("\n" + "="*50)
print("АНАЛИЗ ЗАВЕРШЕН")
print("="*50)
print(f"Итоговый размер данных: {len(df)} строк")ё