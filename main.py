from utils import write_operations

operations = write_operations()
for operation in operations:
    if operation.get_state()!= None:
        print(operation.get_state())