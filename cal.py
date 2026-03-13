from abc import ABC, abstractmethod

class CalculatorBase(ABC):
    @abstractmethod
    def add(self, num1, num2):
        pass
    @abstractmethod
    def subtract(self, num1, num2):
        pass
    @abstractmethod
    def multiply(self, num1, num2):
        pass
    @abstractmethod
    def divide(self, num1, num2):
        pass
    @abstractmethod
    def modulo(self, num1, num2):
        pass
    @abstractmethod
    def power(self, num1, num2):
        pass

class Calculator(CalculatorBase):
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    def modulo(self, num1, num2):
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Modulo by zero"

    def power(self, num1, num2):
        return num1 ** num2


calc = Calculator()

while True:
    print("\n===== CALCULATOR MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Power")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            print("Result:", calc.add(num1, num2))
        elif choice == '2':
            print("Result:", calc.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calc.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calc.divide(num1, num2))
        elif choice == '5':
            print("Result:", calc.modulo(num1, num2))
        elif choice == '6':
            print("Result:", calc.power(num1, num2))
    elif choice == '7':
        print("Thank you for using the calculator")
        break
    else:
        print("Invalid option")
