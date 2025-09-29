# Запрос данных у пользователя
minutes = float(input("Введите число израсходованных минут разговоров: "))
sms =  float(input("Введите число отправленных сообщений: "))
inet = float(input("Введите число израсходованных Мб трафика: "))

# задаем стоимость базового тарифа и его рамок
base_tarif = 24.99
min_base = 60
sms_base = 30
inet_base = 1024

# обрабатываем случай, когда клиент уложился в рамки тарифа
if minutes <= min_base and sms <= sms_base and inet <= inet_base:
    print("Стоимость вашего тарифа: "+ str(base_tarif) + " руб\nВаши расходы в этом месяце: не превысили значения вашего тарифа\nИтого сумма к оплате: "+ str(base_tarif) + " руб ")
    # обрабатываем случай, когда клиент уложился в рамки тарифа
else: 
    # проверяем, какие параметры выше указанных в тарифе
    if minutes <= min_base:
        min_tarif = 0
    else:
        min_tarif = ((0.89*(minutes - min_base))//0.01)*0.01

    if sms <= sms_base:
        sms_tarif = 0
    else:
        sms_tarif = ((0.59*(sms - sms_base))//0.01)*0.01

    if inet <= inet_base:
        inet_tatrif = 0
    else:
        inet_tarif = ((0.79*(inet - inet_base))//0.01)*0.01 

    # считаем итоговый результат превышения
    total_tarif = min_tarif + sms_tarif + inet_tarif

    # считаем налог по сумме превышения
    tax = 0.02
    added_tax = ((total_tarif * tax)//0.01)*0.01

    # считаем итоговый результат превышения + стоимость тарифа
    total_cost = base_tarif + total_tarif + added_tax

    # выводим информацию о превышении ограничений тарифа
    print("Стоимость вашего тарифа: "+ str(base_tarif) + " руб\nВаши расходы в этом месяце: превысили значения вашего тарифа\nДополнительная плата за минуты разговора: " + str(min_tarif) +" \n Дополнительная плата за звонки: "+ str(sms_tarif) +" \n Дополнительная плата за интернет: "+ str(inet_tarif) +" \n Налог за дополнительные услуги: "+str(tax*100)+" %\nИтого сумма к оплате(стоимость тарифа + доп услуги + налог за доп услуги): "+str(base_tarif) +" + "+ str(total_tarif) +" + "+ str(added_tax)+ " = "+ str(total_cost) +" руб ")
