# print(f"""1. Открыть счет для клиента.
# 2. Закрыть счет клиента.
# 3. Пополнить банковский счет.
# 4. Снять сумму со счета.
# 5. Перевести деньги между счетами.
# 6. Выписка по счетам
# 7. Сменить пользователя
# 8. Выход""")
import os

class InsufficientFundsException(Exception):
    pass

class CurrencyMismatchException(Exception):
    pass

class Client:
    def __init__(self, client_id, name, surname):
        self.client_id = client_id
        self.name = name
        self.accounts = {}
        self.surname = surname

class BankAccount:
    def __init__(self, acc_id, client_id, currency, balance=0):
        self.acc_id = acc_id
        self.client_id = client_id
        self.currency = currency
        self.balance = balance  

class Bank():
    def __init__(self):
        self.clients = {}
        
    def add_client(self, client_id, name, surname):
        if client_id not in self.clients:
            self.clients[client_id] = Client(client_id, name, surname)

    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")

        for account in self.clients[client_id].accounts.values(): # здесь может быть ошибка обращения к id
            if account.acc_id == f"{client_id}{currency}":
                raise ValueError("Счет в этой валюте уже существует")

        acc_id = f"{client_id}{currency.upper()}"
        # print(acc_id)
        self.clients[client_id].accounts[acc_id] = BankAccount(acc_id,client_id, currency, balance = 0)
    
    def close_account(self, acc_id, client_id):
        # print(f"{client_id} {acc_id}")
        account = self.clients[client_id].accounts.get(acc_id)
        if not account:
            raise ValueError("Счет не найден")
        if account.client_id != client_id:
            raise PermissionError("Доступ запрещен")
        if account.balance != 0:
            raise ValueError("Невозможно закрыть счет с ненулевым балансом")
        
        del self.clients[client_id].accounts[acc_id]

    def deposit(self, acc_id, amount, client_id):
        print( acc_id[0:-3])
        if int(acc_id[0:-3]) != client_id:
            raise ValueError("Данный счет не принадлежит данному клиенту.")
        # client_id = int(acc_id[0:-3])
        account = self.clients[client_id].accounts.get(acc_id)
        if not account:
            raise ValueError("Счет не найден")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        
        account.balance += amount

    def withdraw(self, acc_id, amount, client_id):
        account = self.clients[client_id].accounts.get(acc_id)
        if not account:
            raise ValueError("Счет не найден")
        if account.client_id != client_id:
            raise PermissionError("Доступ запрещен")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if account.balance < amount:
            raise InsufficientFundsException("Недостаточно средств")
        
        account.balance -= amount

    def transfer(self, from_account, to_account, amount, client_id_f, client_id_t):
        
        if from_account not in self.clients[client_id_f].accounts or to_account not in self.clients[client_id_t].accounts:
            raise ValueError("Один из счетов не найден")
        
        from_acc = self.clients[client_id_f].accounts[from_account]
        to_acc = self.clients[client_id_t].accounts[to_account]
        
        if from_acc.client_id != client_id_f:
            raise PermissionError("Доступ запрещен")
        if from_acc.currency != to_acc.currency:
            raise CurrencyMismatchException("Валюты счетов не совпадают")
        if from_acc.balance < amount:
            raise InsufficientFundsException("Недостаточно средств")
        
        from_acc.balance -= amount
        to_acc.balance += amount

    def get_client_accounts(self, client_id):
        return [acc for acc in self.clients[client_id].accounts.values() if acc.client_id == client_id]        

def save_statement(client, accounts, filename=None):
    if not filename:
        filename = f"выписка_{client.client_id}.txt"
    
    total_balance = sum(acc.balance for acc in accounts)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Выписка по счетам клиента: {client.name} {client.surname}\n")
        f.write("=" * 50 + "\n")
        for acc in accounts:
            f.write(f"Счет №{acc.acc_id} ({acc.currency}): {acc.balance:.2f}\n")
        f.write("=" * 50 + "\n")
        f.write(f"Общий баланс: {total_balance:.2f}\n")


def main():
    bank = Bank()
    bank.add_client(1, "Иван", "Иванов")
    bank.add_client(2, "Петр", "Петров")
    
    bank.open_account(1, "RUB")
    bank.open_account(1, "USD")
    bank.open_account(2, "RUB")
    # ...
    current_client = None
    
    while True:
        if not current_client:
            try:
                client_id = int(input("Введите ваш ID клиента: "))
                if client_id not in bank.clients:
                    print("Ошибка: Клиент с таким ID не найден")
                    continue
                current_client = bank.clients[client_id]
            except ValueError:
                print("Ошибка: Введите корректный ID (число)")
                continue

        print("\n" + "=" * 30)
        print("Банковская система")
        print("1. Открыть счет")
        print("2. Закрыть счет")
        print("3. Пополнить счет")
        print("4. Снять со счета")
        print("5. Перевести средства")
        print("6. Выписка по счетам")
        print("7. Сменить пользователя")
        print("8. Выход")
        
        choice = input("Выберите действие: ")
        
        try:
            if choice == '1':
                currency = input("Введите валюту счета: ").upper()
                new_account = bank.open_account(current_client.client_id, currency)
                print(f"Счет №{new_account} в валюте {currency} успешно открыт")
                
            elif choice == '2':
                acc_id = str(input("Введите номер счета('(ваш_ID)(валюта_счета_БОЛЬШИМИБУКВАМИ)'): "))
                bank.close_account(acc_id, current_client.client_id)
                print("Счет успешно закрыт")
                
            elif choice == '3':
                acc_id = str(input("Введите номер счета('(ваш_ID)(валюта_счета_БОЛЬШИМИБУКВАМИ)'): "))
                amount = float(input("Введите сумму пополнения: "))
                bank.deposit(acc_id, amount, client_id)
                print("Счет успешно пополнен")
                
            elif choice == '4':
                acc_id = str(input("Введите номер счета('(ваш_ID)(валюта_счета_БОЛЬШИМИБУКВАМИ)'): "))
                amount = float(input("Введите сумму для снятия: "))
                bank.withdraw(acc_id, amount, current_client.client_id)
                print("Средства успешно сняты")
                
            elif choice == '5':
                from_acc = str(input("Введите номер счета, с которого вы хотите перевести('(ваш_ID)(валюта_счета_БОЛЬШИМИБУКВАМИ)'): "))
                to_acc = str(input("Введите номер счета, на который вы хотите перевести('(ваш_ID)(валюта_счета_БОЛЬШИМИБУКВАМИ)'): "))
                amount = float(input("Введите сумму перевода: "))
                bank.transfer(from_acc, to_acc, amount, current_client.client_id, int(to_acc[0:-3]))
                print("Перевод успешно выполнен")
                
            elif choice == '6':
                accounts = bank.get_client_accounts(current_client.client_id)
                save_statement(current_client, accounts)
                print("Выписка сохранена в файл")
                
            elif choice == '7':
                current_client = None
                print("Вы вышли из системы")
                
            elif choice == '8':
                answ = int(input("Вы уверены, что хотите выйти из системы?(введите 0(нет) или 1(да))"))
                if answ == 0:
                    main()
                elif answ != 1:
                    print("Вы неправильно ввели значение, возврат в систему...")
                    main()
                else:
                    print("Выход из системы...")
                break
                
            else:
                print("Неверный выбор")
                
        except (ValueError, PermissionError, InsufficientFundsException, CurrencyMismatchException) as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()



# ID счета - это ID клиента + валюта счета 
# добавить конвертацию валют при взаимодействии счетов разных валют
# предусмотреть ввод ID счета через буквы разного регистра
