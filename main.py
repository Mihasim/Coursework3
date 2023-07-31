from utils import write_operations

operations = write_operations()
for operation in operations:
    if operation.print_operation() != None:
            print(operation.print_operation())
