from collections import UserDict

""" базовий клас Field для обробки загальних фукцій полів"""
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        """ 
        Перетворюємо значення поля на рядкове представлення 
        """
        return str(self.value)

  
""" клас Name успадковвує Field, представляє ім'я контакту """
class Name(Field):
    pass

""" клас Phone успадковвує Field, представляє номер телефону контакту"""
class Phone(Field):
    
    """ініціалізуємо телефон з переввіркою на 10-значний номер"""
    def __init__(self, value):
        if not value.isdigit() and len(value) != 10:
            raise ValueError ("Invalid phone number. Must contain exactly 10 digits")
        super().__init__(value) #викликає конструктор Field для збереження значенння

"""клас Record для обробки інформаціі про окремий контакт"""
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone_value):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]
        
    def edit_phone(self, old_phone_value, new_phone_value):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone_value:
                self.phones [i] = Phone(new_phone_value)
                return
        raise ValueError("Phone number not found")    
        
    def find_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                return phone
        return None

    def __str__(self): # рядкове предсталення телефону 
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

# клас AddressBook успадковує UserDict, є колекцією записів
class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found")
    
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

    
    
    
    