#Задание1
class PostalAddress:
    def __init__(self, street, house, apartment):
        self.street = street
        self.house = house
        self.apartment = apartment

    def get_street(self):
        return self.street

    def set_street(self, street):
        self.street = street

    def get_house(self):
        return self.house

    def set_house(self, house):
        self.house = house

    def get_apartment(self):
        return self.apartment

    def set_apartment(self, apartment):
        self.apartment = apartment

address1 = PostalAddress("Ленина, 45", "дом 1", "квартира 123")
address2 = PostalAddress("Мира 12", "дом 2", "квартира 54")

print("Адрес 1: улица - {address1.street}, дом - {address1.house}, квартира - {address1.apartment}")
print("Адрес 2: улица - {address2.street}, дом - {address2.house}, квартира - {address2.apartment}")


###################################################################################################################

#Задание2

class Address:
    def __init__(self, street: str, house: int, apartment: int = None):
        self._street = None
        self._house = None
        self._apartment = None
        self.street = street
        self.house = house
        self.apartment = apartment


    def street(self):
        return self._street


    def street(self, value):
        if value.startswith('ул'):
            self._street = 'ул'
        elif value.startswith('пр'):
            self._street = 'пр'
        elif value.startswith('пер'):
            self._street = 'пер'
        else:
            raise ValueError('Неверное название улицы')


    def house(self):
        return self._house


    def house(self, value):
        if self._street == 'пер' and (value < 1 or value > 30):
            raise ValueError('Номер дома на переулке должен быть от 1 до 30')
        elif self._street == 'ул' and (value < 1 or value > 100):
            raise ValueError('Номер дома на улице должен быть от 1 до 100')
        elif self._street == 'пр' and (value < 1 or value > 1000):
            raise ValueError('Номер дома на проспекте должен быть от 1 до 1000')
        else:
            self._house = value


    def apartment(self):
        return self._apartment


    def apartment(self, value):
        if value is not None and self._street == 'пер':
            raise ValueError('В переулке нет квартир')
        else:
            self._apartment = value

# Использование класса
# Создание объектов с заданными значениями
address1 = Address('ул Ленина', 50, 15)
address2 = Address('пер Внеземной', 10)

# Получение и изменение значений полей
print(address1.street)  # выведет 'ул'
address1.street = 'ул Чертыгашева'
print(address1.street)  # выведет 'ул'

print(address1.house)  # выведет 50
address1.house = 120  # вызовет исключение ValueError, так как на улице номера домов от 1 до 100
address1.house = 70
print(address1.house)  # выведет 70

print(address1.apartment)  # выведет 15
address1.apartment = None
print(address1.apartment)  # выведет None

# Пример нарушения ограничений
address2.house = 35  # вызовет исключение ValueError, так как в переулке номера домов от 1 до 30
address2.apartment = 5  # вызовет исключение ValueError, так как в переулке нет квартир;