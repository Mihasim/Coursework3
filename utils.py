import json
import datetime


def load_operaion():
    """
    Загрузка данных из файла operations.json
    :return: список словарей
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def sort_operations():
    """
    сортировка списка словарей по дате
    :return: список словарей
    """
    sorted_operation = load_operaion()
    sorted_operation = sorted(sorted_operation, key=lambda k: k['date'], reverse=True)
    return sorted_operation

def get_five():
    """
    Получает первые 5 исполненных операций
    :return:
    """
    five_executed_oper = []
    i = 0

    for operations in sort_operations():
        if operations["state"] == "EXECUTED":
            five_executed_oper.append(operations)
            i += 1
        if i == 5:
            break
    return five_executed_oper


class Operations:

    def __init__(self, date, description, to_card, amount, name, state, from_card=None):
        self.date = date
        self.description = description
        self.from_card = from_card
        self.to_card = to_card
        self.amount = amount
        self.name = name
        self.state = state


    def print_operation(self):
        """
        Выводит на экран форму вывода
        """
        print(f"{self.date} {self.description} \n"
              f"{self.from_card} -> {self.to_card}\n"
              f"{self.amount} {self.name}\n")



    def __repr__(self):
        return f"{self.date, self.description, self.from_card, self.to_card, self.amount, self.name, self.state}"


def mask(kode):
    """
    Маскирует данные карты
    :return: название и замаскированный номер в виде строки
    """
    list_kode = kode.split()
    kard_words = []
    for kode in list_kode:

        if kode.isalpha():
            kard_words.append(kode)

        if kode.isdigit():
            pices = [kode[i:i+4] for i in range(0, len(kode), 4)]
            whole = " ".join(pices)
            whole = whole[0:7] + "** **** " + whole[-4:len(whole)]

    whole_word = " ".join(kard_words)
    whole_kode = f"{whole_word} {whole}"
    return whole_kode

def write_operations():
    """
    Получаем данные об операциях из файла operations.json и добавляем их в экземпляр класса Operations
    :return: список экземпляров класса Operations
    """
    operations = []
    for operation in get_five():
        date = operation["date"]
        #Переводим дату в необходимый формат
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = operation["description"]
        #проверяем производится перевод или открытие вклада
        if "from" in operation:
            from_card = mask(operation["from"])
        else:
            from_card = "Открытие вклада"
        to_card = mask(operation["to"])
        amount = operation["operationAmount"]["amount"]
        name = operation["operationAmount"]["currency"]["name"]
        state = operation["state"]
        operations.append(Operations(date, description, to_card, amount, name, state, from_card))
    return operations


