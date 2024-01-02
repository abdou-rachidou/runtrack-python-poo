class Operation:


    def __init__(self, nombre1, nombre2) -> None:
        self.my_number1 = nombre1
        self.my_number2 = nombre2
        pass

    def addition(self):
        print(self.my_number1 + self.my_number2)


result = Operation(12, 3)
result.addition()