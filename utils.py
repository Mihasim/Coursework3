import json
import datetime


def load_operaion():
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
        print(f"{self.date} {self.description} \n"
              f"{self.from_card} -> {self.to_card}\n"
              f"{self.amount} {self.name}\n")

    def get_state(self):
        if self.state == "EXECUTED":
            self.print_operation()

    def __repr__(self):
        return f"{self.date, self.description, self.from_card, self.to_card, self.amount, self.name, self.state}"


def write_operations():
    operations = []
    for operation in load_operaion():
        if "date" in operation:
            date = operation["date"]
            #Переводим дату в необходимый формат
            date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%y")

        if "description" in operation:
            description = operation["description"]

        if "from" in operation:
            from_card = operation["from"]
        else:
            from_card = "Открытие вклада"

        if "to" in operation:
            to_card = operation["to"]

        if "operationAmount" in operation:
            amount = operation["operationAmount"]["amount"]

        if "operationAmount" in operation:
            name = operation["operationAmount"]["currency"]["name"]

        if "state" in operation:
            state = operation["state"]

        operations.append(Operations(date, description, to_card, amount, name, state, from_card))
    return operations


