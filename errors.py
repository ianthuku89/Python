#using try except block
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

