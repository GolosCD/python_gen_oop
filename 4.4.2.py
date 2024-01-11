'''
Класс BankAccount
Реализуйте класс BankAccount, описывающий банковский счет. 
При создании экземпляра класс должен принимать один аргумент:

balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:

_balance — баланс счета
Класс BankAccount должен иметь четыре метода экземпляра:

get_balance() — метод, возвращающий актуальный баланс счета
deposit() — метод, принимающий в качестве аргумента число amount и 
увеличивающий баланс счета на amount
withdraw() — метод, принимающий в качестве аргумента число amount и 
уменьшающий баланс счета на amount. Если amount превышает количество средств 
на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
На счете недостаточно средств
transfer() — метод, принимающий в качестве аргументов банковский счет account 
и число amount. Метод должен уменьшать баланс текущего счета на amount и 
увеличивать баланс счета account на amount. Если amount превышает количество 
средств на балансе текущего счета, должно быть возбуждено исключение ValueError 
с сообщением:
На счете недостаточно средств
Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется. 
Гарантируется, что реализованный класс используется только с корректными данными.
'''

class BlankAccount:
    def __init__(self,balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
        
    def deposit(self,amount):
        self._balance += amount
        
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance -= amount
        else:
            raise ValueError('На счете недостаточно средств')
    
    def transfer(self,account,amount):
        self.withdraw(amount)
        account.deposit(amount)
        
        