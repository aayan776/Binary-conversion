number = int(input("Enter number to covert: "))
def calculate(number):
    result = bin(number).replace("0b", "")
    print(f"The binary form of {number} is {result}")
calculate(number)