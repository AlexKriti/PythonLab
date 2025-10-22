# Запрос данных у пользователя
pressure = float(input("Давление (P>0) в Паскалях (Пс): "))
volume = float(input("Объем (V>0) в метрах кубических (м3): "))
temperature = float(input("Температура (T>0) в градусах Кельвина (°K): "))

# проверка введенных значений
if pressure <= 0 or volume <= 0 or temperature <= 0:
    print("Вы ввели некорректное/ые значение/ия")
    raise ValueError("Null catch")

# Универсальная газовая постоянная в (Пс * м3)/(моль·K)
R = 8.31

# Расчет количества вещества по формуле: n = PV / RT
n = (pressure * volume) / (R * temperature)
        
# Вывод результата
print("Результат расчета:")
print("Давление: "+str(pressure)+" Пс")
print("Объем: "+str(volume)+" м3")
print("Температура: "+str(temperature)+" K")
print("Универсальная газовая постоянная R = "+ str(R) +" (Пс * м3)/(моль·K)")
print("Количество газа: "+ str(n) +" моль")