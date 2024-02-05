from random import randint, sample
from datetime import datetime, timedelta
from main import AddressBook, Birthday, Name, Phone


class RecordGenerator:
    @staticmethod
    def generate_name():
        # Генеруємо випадкове ім'я
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        return ''.join(sample(letters, randint(3, 10)))

    @staticmethod
    def generate_phone():
        return ''.join(str(randint(0, 9)) for _ in range(10))

    @staticmethod
    def generate_birthday():
        start_date = datetime(1980, 1, 1)
        end_date = datetime(2000, 12, 31)
        random_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
        return random_date.strftime("%d-%m-%Y")

    @classmethod
    def generate_record(cls):
        name = cls.generate_name()
        phone = cls.generate_phone()
        birthday = cls.generate_birthday()
        return Record(name, phone, birthday)


class Record:
    def __init__(self, name, phone, birthday):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {self.phone.value}, birthday: {self.birthday.value}"


# Генеруємо 100 записів
records = [RecordGenerator.generate_record() for _ in range(100)]

# Додаємо їх до AddressBook
address_book = AddressBook()
for record in records:
    address_book.add_record(record)

# Використовуємо метод iterator
for page in address_book.iterator(page_size=5):
    for record in page:
        print(record)
    print('-' * 30)  # Додатковий рядок для розділення між
