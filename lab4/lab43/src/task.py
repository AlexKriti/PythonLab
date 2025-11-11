import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import random
import os

# Настройка для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

class AdmissionDataGenerator:
    """
    Класс для генерации синтетических данных о вступительной кампании
    """
    
    def __init__(self, seed=42):
        self.seed = seed
        np.random.seed(seed)
        random.seed(seed)
        
        # Базы данных для генерации
        self.first_names = ['Александр', 'Алексей', 'Андрей', 'Артем', 'Борис', 'Вадим', 'Василий', 'Виктор', 
                           'Владимир', 'Дмитрий', 'Евгений', 'Иван', 'Игорь', 'Кирилл', 'Максим', 'Михаил',
                           'Никита', 'Олег', 'Павел', 'Роман', 'Сергей', 'Юрий', 'Анастасия', 'Анна', 
                           'Валерия', 'Вероника', 'Виктория', 'Галина', 'Дарья', 'Екатерина', 'Елена',
                           'Ирина', 'Ксения', 'Мария', 'Наталья', 'Ольга', 'Светлана', 'Татьяна', 'Юлия']
        
        self.last_names = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 
                          'Федоров', 'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров',
                          'Павлов', 'Козлов', 'Степанов', 'Николаев', 'Орлов', 'Андреев', 'Макаров',
                          'Захаров', 'Зайцев', 'Соловьев', 'Борисов', 'Яковлев', 'Григорьев', 'Романов']
        
        self.middle_names = ['Александрович', 'Алексеевич', 'Андреевич', 'Артемович', 'Борисович', 
                            'Вадимович', 'Васильевич', 'Викторович', 'Владимирович', 'Дмитриевич',
                            'Евгеньевич', 'Иванович', 'Игоревич', 'Кириллович', 'Максимович', 'Михайлович',
                            'Никитич', 'Олегович', 'Павлович', 'Романович', 'Сергеевич', 'Юрьевич',
                            'Александровна', 'Алексеевна', 'Андреевна', 'Артемовна', 'Борисовна', 
                            'Вадимовна', 'Васильевна', 'Викторовна', 'Владимировна', 'Дмитриевна',
                            'Евгеньевна', 'Ивановна', 'Игоревна', 'Кирилловна', 'Максимовна', 'Михайловна',
                            'Никитична', 'Олеговна', 'Павловна', 'Романовна', 'Сергеевна', 'Юрьевна']
        
        self.specialties = {
            'Информатика': ['Математика', 'Физика', 'Информатика'],
            'Физика': ['Математика', 'Физика', 'Информатика'],
            'Математика': ['Математика', 'Физика', 'Иностранный язык'],
            'Химия': ['Химия', 'Биология', 'Математика'],
            'Биология': ['Биология', 'Химия', 'Математика'],
            'Экономика': ['Математика', 'Иностранный язык', 'Обществоведение'],
            'Юриспруденция': ['Обществоведение', 'История', 'Иностранный язык'],
            'Медицина': ['Биология', 'Химия', 'Математика'],
            'Лингвистика': ['Иностранный язык', 'Русский язык', 'История'],
            'Психология': ['Биология', 'Математика', 'Обществоведение']
        }
        
        self.cities = ['Минск', 'Гомель', 'Могилев', 'Витебск', 'Гродно', 'Брест', 
                      'Барановичи', 'Борисов', 'Пинск', 'Орша', 'Мозырь', 'Солигорск',
                      'Новополоцк', 'Лида', 'Молодечно', 'Полоцк', 'Жлобин', 'Речица']
        
        self.study_forms = ['бюджет', 'платное', 'целевое']
        
    def generate_fio(self):
        """Генерация ФИО"""
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        
        # Определяем пол по имени (женские имена начинаются с индекса 22)
        is_female = first_name in self.first_names[22:]
        
        # Выбираем отчество в зависимости от пола
        if is_female:
            middle_name = random.choice([mn for mn in self.middle_names if mn.endswith('на')])
        else:
            middle_name = random.choice([mn for mn in self.middle_names if mn.endswith('ич')])
            
        return f"{last_name} {first_name} {middle_name}"
    
    def generate_phone(self):
        """Генерация номера телефона"""
        return f"+37529{random.randint(1000000, 9999999)}"
    
    def generate_address(self):
        """Генерация адреса"""
        city = random.choice(self.cities)
        streets = ['Ленина', 'Советская', 'Победы', 'Мира', 'Гагарина', 'Кирова', 'Фрунзе']
        street = random.choice(streets)
        house = random.randint(1, 100)
        return f"г. {city}, ул. {street}, д. {house}"
    
    def generate_scores(self, specialty):
        """Генерация баллов для специальности"""
        subjects = self.specialties[specialty]
        
        # Баллы ЦТ (0-100)
        ct_scores = {}
        for subject in ['Математика', 'Физика', 'Химия', 'Биология', 'История', 
                       'Обществоведение', 'Русский язык', 'Иностранный язык', 'Информатика']:
            if subject in subjects:
                # Баллы по профильным предметам выше
                ct_scores[subject] = np.random.normal(75, 10)
            else:
                ct_scores[subject] = np.random.normal(60, 15)
            
            # Ограничиваем баллы от 0 до 100
            ct_scores[subject] = max(0, min(100, ct_scores[subject]))
        
        # Средний балл аттестата (1-10)
        certificate_score = np.random.normal(7.5, 1.2)
        certificate_score = max(1, min(10, certificate_score))
        
        # Общий балл (сумма баллов по трем предметам + балл аттестата * 10)
        main_scores = [ct_scores[subject] for subject in subjects]
        total_score = sum(main_scores) + certificate_score * 10
        
        return ct_scores, certificate_score, total_score
    
    def generate_student(self, year):
        """Генерация данных одного студента"""
        specialty = random.choice(list(self.specialties.keys()))
        
        ct_scores, certificate_score, total_score = self.generate_scores(specialty)
        
        # Форма обучения с разной вероятностью
        study_form_weights = [0.5, 0.4, 0.1]  # бюджет, платное, целевое
        study_form = random.choices(self.study_forms, weights=study_form_weights)[0]
        
        student_data = {
            'ФИО': self.generate_fio(),
            'Год поступления': year,
            'Форма обучения': study_form,
            'Средний балл аттестата': certificate_score,
            'Общий балл': total_score,
            'Специальность': specialty,
            'Адрес регистрации': self.generate_address(),
            'Телефон': self.generate_phone()
        }
        
        # Добавляем баллы по предметам
        student_data.update(ct_scores)
        
        return student_data
    
    def generate_dataset(self, years=5, students_per_year=200):
        """Генерация полного набора данных"""
        current_year = datetime.now().year
        years_range = range(current_year - years + 1, current_year + 1)
        
        data = []
        for year in years_range:
            for _ in range(students_per_year):
                data.append(self.generate_student(year))
        
        return pd.DataFrame(data)

class AdmissionDataVisualizer:
    """
    Класс для визуализации данных о вступительной кампании
    """
    
    def __init__(self, df, output_dir="plots"):
        self.df = df
        self.output_dir = output_dir
        self.setup_plot_style()
        self.create_output_dir()
    
    def create_output_dir(self):
        """Создает директорию для сохранения графиков"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def setup_plot_style(self):
        """Настройка стиля графиков"""
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def save_plot(self, filename):
        """Сохраняет текущий график в файл"""
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"График сохранен: {filepath}")
        plt.close()  # Закрываем фигуру после сохранения
    
    def plot_ct_scores_dynamics(self):
        """Динамика среднего балла за ЦТ по предметам"""
        subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'История', 
                   'Обществоведение', 'Русский язык', 'Иностранный язык', 'Информатика']
        
        fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        axes = axes.flatten()
        
        for i, subject in enumerate(subjects):
            if i < len(axes):
                subject_data = self.df.groupby('Год поступления')[subject].mean()
                axes[i].plot(subject_data.index, subject_data.values, marker='o', linewidth=2)
                axes[i].set_title(f'{subject}', fontsize=12, fontweight='bold')
                axes[i].set_xlabel('Год')
                axes[i].set_ylabel('Средний балл')
                axes[i].grid(True, alpha=0.3)
                axes[i].tick_params(axis='x', rotation=45)
        
        # Убираем лишние subplots
        for i in range(len(subjects), len(axes)):
            fig.delaxes(axes[i])
        
        plt.suptitle('Динамика среднего балла за ЦТ по предметам', fontsize=16, fontweight='bold')
        plt.tight_layout()
        self.save_plot('ct_scores_dynamics.png')
    
    def plot_certificate_scores_dynamics(self):
        """Динамика среднего балла аттестата"""
        plt.figure(figsize=(12, 6))
        
        cert_data = self.df.groupby('Год поступления')['Средний балл аттестата'].mean()
        
        plt.plot(cert_data.index, cert_data.values, marker='o', linewidth=3, 
                markersize=8, color='#2E8B57')
        plt.fill_between(cert_data.index, cert_data.values, alpha=0.3, color='#2E8B57')
        
        plt.title('Динамика среднего балла аттестата', fontsize=16, fontweight='bold')
        plt.xlabel('Год поступления')
        plt.ylabel('Средний балл аттестата')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # Добавляем аннотации с значениями
        for year, score in cert_data.items():
            plt.annotate(f'{score:.2f}', (year, score), 
                        textcoords="offset points", xytext=(0,10), ha='center')
        
        plt.tight_layout()
        self.save_plot('certificate_scores_dynamics.png')
    
    def plot_passing_scores_dynamics(self):
        """Динамика проходного балла по специальностям"""
        plt.figure(figsize=(14, 8))
        
        # Проходной балл = минимальный общий балл поступивших на специальность
        passing_scores = self.df.groupby(['Год поступления', 'Специальность'])['Общий балл'].min().unstack()
        
        for specialty in passing_scores.columns:
            plt.plot(passing_scores.index, passing_scores[specialty], 
                    marker='o', linewidth=2, label=specialty)
        
        plt.title('Динамика проходного балла по специальностям', fontsize=16, fontweight='bold')
        plt.xlabel('Год поступления')
        plt.ylabel('Проходной балл')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.save_plot('passing_scores_dynamics.png')
    
    def plot_students_by_specialty(self):
        """Количество поступивших студентов по специальностям"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Общее количество по специальностям
        specialty_counts = self.df['Специальность'].value_counts()
        ax1.bar(specialty_counts.index, specialty_counts.values, color=sns.color_palette("Set3"))
        ax1.set_title('Общее количество студентов по специальностям', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Специальность')
        ax1.set_ylabel('Количество студентов')
        ax1.tick_params(axis='x', rotation=45)
        
        # Добавляем значения на столбцы
        for i, v in enumerate(specialty_counts.values):
            ax1.text(i, v + 0.5, str(v), ha='center', va='bottom')
        
        # Динамика по годам
        yearly_specialty = pd.crosstab(self.df['Год поступления'], self.df['Специальность'])
        yearly_specialty.plot(kind='bar', stacked=True, ax=ax2, colormap='Set3')
        ax2.set_title('Динамика поступления по специальностям', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Год поступления')
        ax2.set_ylabel('Количество студентов')
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        self.save_plot('students_by_specialty.png')
    
    def plot_study_forms_statistics(self):
        """Статистика по формам обучения"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Общая статистика
        form_counts = self.df['Форма обучения'].value_counts()
        colors = ['#4CAF50', '#FF9800', '#2196F3']  # зеленый, оранжевый, синий
        wedges, texts, autotexts = ax1.pie(form_counts.values, labels=form_counts.index, 
                                          autopct='%1.1f%%', colors=colors, startangle=90)
        ax1.set_title('Распределение по формам обучения', fontsize=14, fontweight='bold')
        
        # Улучшаем отображение текста
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        # Динамика по годам
        yearly_forms = pd.crosstab(self.df['Год поступления'], self.df['Форма обучения'])
        yearly_forms.plot(kind='bar', ax=ax2, color=colors)
        ax2.set_title('Динамика форм обучения по годам', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Год поступления')
        ax2.set_ylabel('Количество студентов')
        ax2.legend(title='Форма обучения')
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        self.save_plot('study_forms_statistics.png')
    
    def plot_comprehensive_analysis(self):
        """Комплексный анализ данных"""
        fig = plt.figure(figsize=(16, 12))
        
        # 1. Тепловая карта корреляций баллов
        plt.subplot(2, 2, 1)
        subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'История', 
                   'Русский язык', 'Иностранный язык', 'Информатика']
        correlation_matrix = self.df[subjects + ['Средний балл аттестата', 'Общий балл']].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                   square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
        plt.title('Корреляция между баллами', fontsize=12, fontweight='bold')
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)
        
        # 2. Распределение общего балла
        plt.subplot(2, 2, 2)
        sns.histplot(data=self.df, x='Общий балл', hue='Форма обучения', 
                    multiple="stack", palette='Set2')
        plt.title('Распределение общего балла по формам обучения', fontsize=12, fontweight='bold')
        plt.xlabel('Общий балл')
        plt.ylabel('Количество студентов')
        
        # 3. Баллы по топ-5 специальностям
        plt.subplot(2, 2, 3)
        top_specialties = self.df['Специальность'].value_counts().head(5).index
        top_data = self.df[self.df['Специальность'].isin(top_specialties)]
        sns.boxplot(data=top_data, x='Специальность', y='Общий балл', palette='pastel')
        plt.title('Распределение общего балла по топ-специальностям', fontsize=12, fontweight='bold')
        plt.xlabel('Специальность')
        plt.ylabel('Общий балл')
        plt.xticks(rotation=45)
        
        # 4. Средний балл аттестата по годам и формам обучения
        plt.subplot(2, 2, 4)
        cert_year_form = self.df.groupby(['Год поступления', 'Форма обучения'])['Средний балл аттестата'].mean().unstack()
        cert_year_form.plot(kind='line', marker='o', ax=plt.gca())
        plt.title('Динамика среднего балла аттестата по формам обучения', fontsize=12, fontweight='bold')
        plt.xlabel('Год поступления')
        plt.ylabel('Средний балл аттестата')
        plt.grid(True, alpha=0.3)
        plt.legend(title='Форма обучения')
        
        plt.suptitle('Комплексный анализ данных вступительной кампании', fontsize=16, fontweight='bold')
        plt.tight_layout()
        self.save_plot('comprehensive_analysis.png')
    
    def generate_all_visualizations(self):
        """Генерация всех визуализаций"""
        print("Генерация визуализаций...")
        
        self.plot_ct_scores_dynamics()
        self.plot_certificate_scores_dynamics()
        self.plot_passing_scores_dynamics()
        self.plot_students_by_specialty()
        self.plot_study_forms_statistics()
        self.plot_comprehensive_analysis()
        
        print("Все графики сохранены в папку 'plots'")

def main():
    """
    Основная функция программы
    """
    print("ГЕНЕРАЦИЯ ДАННЫХ О ВСТУПИТЕЛЬНОЙ КАМПАНИИ")
    print("=" * 50)
    
    # Генерация данных
    print("Генерация синтетических данных...")
    generator = AdmissionDataGenerator(seed=42)
    df = generator.generate_dataset(years=5, students_per_year=200)
    
    print(f"Сгенерировано записей: {len(df)}")
    print(f"Период: {df['Год поступления'].min()} - {df['Год поступления'].max()} гг.")
    print(f"Количество специальностей: {df['Специальность'].nunique()}")
    print()
    
    # Базовая статистика
    print("Базовая статистика:")
    print(f"Средний общий балл: {df['Общий балл'].mean():.2f}")
    print(f"Средний балл аттестата: {df['Средний балл аттестата'].mean():.2f}")
    print(f"Распределение по формам обучения:")
    print(df['Форма обучения'].value_counts())
    print()
    
    # Визуализация
    print("Создание визуализаций...")
    visualizer = AdmissionDataVisualizer(df)
    visualizer.generate_all_visualizations()
    
    # Сохранение данных
    output_file = 'admission_data.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Данные сохранены в файл: {output_file}")
    
    # Дополнительная информация
    print("\n=== РЕЗЮМЕ ===")
    print("✅ Данные успешно сгенерированы")
    print("✅ Графики сохранены в папку 'plots'")
    print("✅ CSV файл с данными создан")
    print("\nФайлы:")
    print("- admission_data.csv - исходные данные")
    print("- plots/ - папка с графиками")
    print("  - ct_scores_dynamics.png - динамика баллов ЦТ")
    print("  - certificate_scores_dynamics.png - динамика баллов аттестата")
    print("  - passing_scores_dynamics.png - проходные баллы")
    print("  - students_by_specialty.png - распределение по специальностям")
    print("  - study_forms_statistics.png - формы обучения")
    print("  - comprehensive_analysis.png - комплексный анализ")

if __name__ == "__main__":
    main()