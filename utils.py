import json
import datetime


def load_operaion():
    """
    Загрузка данных из файла operations.json
    :return: список словарей
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


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

    def get_state(self):
        """
        Отбирает только исполненные операции
        :return:
        """
        if self.state == "EXECUTED":
            self.print_operation()

    def __repr__(self):
        return f"{self.date, self.description, self.from_card, self.to_card, self.amount, self.name, self.state}"


def write_operations():
    """
    Получаем данные об операциях из файла operations.json и добавляем их в экземпляр класса Operations
    :return: список экземпляров класса Operations
    """
    operations = []
    for operation in load_operaion():
        date = operation["date"]
        #Переводим дату в необходимый формат
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = operation["description"]
        #проверяем производится перевод или открытие вклада
        if "from" in operation:
            from_card = operation["from"]
        else:
            from_card = "Открытие вклада"
        to_card = operation["to"]
        amount = operation["operationAmount"]["amount"]
        name = operation["operationAmount"]["currency"]["name"]
        state = operation["state"]
        operations.append(Operations(date, description, to_card, amount, name, state, from_card))
    return operations


