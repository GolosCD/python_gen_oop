'''
Классы BasicPlan и подклассы
1. Реализуйте класс BasicPlan, описывающий подписку базового уровня на некотором онлайн-сервисе. При создании экземпляра класс не должен принимать никаких аргументов.

Класс BasicPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение False
 has_UHD — атрибут, имеющий значение False
num_of_devices — атрибут, имеющий значение 1
price — атрибут, имеющий значение 8.99$
2. Также реализуйте класс SilverPlan, наследника класса BasicPlan, описывающий подписку среднего уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса SilverPlan должен совпадать с процессом создания экземпляра класса BasicPlan.

Класс SilverPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение True
 has_UHD — атрибут, имеющий значение False
num_of_devices — атрибут, имеющий значение 2
price — атрибут, имеющий значение 12.99$
3. Наконец, реализуйте класс GoldPlan, наследника класса BasicPlan, описывающий подписку высокого уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса GoldPlan должен совпадать с процессом создания экземпляра класса BasicPlan.

Класс GoldPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение True
 has_UHD — атрибут, имеющий значение True
num_of_devices — атрибут, имеющий значение 4
price — атрибут, имеющий значение 15.99$
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
'''

class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'
        
class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'
    
class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'
        
print(SilverPlan.can_stream)
print(SilverPlan.can_download)
print(SilverPlan.has_SD)
print(SilverPlan.has_HD)
print(SilverPlan.has_UHD)
print(SilverPlan.num_of_devices)
print(SilverPlan.price) 