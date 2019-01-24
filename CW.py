def main():
    # ex1()
    # ex2()
    # ex3()
    ex4()


def add(n1, n2):
    return (n1 + n2)


def subtract(n1, n2):
    return (n1 - n2)


def multiply(n1, n2):
    return (n1 * n2)


def divide(n1, n2):
    return (n1 / n2)



def plus(n1, n2):
    return f'{n1},{n2} addition = {n1 + n2}'

def minus(n1, n2):
    return f'{n1},{n2} subtraction = {n1 - n2}'

def times(n1, n2):
    return f'{n1},{n2} multiplication = {n1 * n2}'

def division(n1, n2):
    return f'{n1},{n2} division = {n1 + n2}'


# Create a function in your program that counts from 0 to [NUMBER]
def ex1():
    number = 40
    for i in range(0, number + 1, 1):
        print(i)


# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def ex2():
    userInput = ""
    while (userInput.lower() != "q"):
        userInput = input("ENTER")


# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform
# the name of the function to the two numbers and return the result.
def ex3():


    n1 = int(input("Enter a number"))
    n2 = int(input("Enter another number"))
    print(add(n1, n2))
    print(subtract(n1, n2))
    print(multiply(n1, n2))
    print(divide(n1, n2))


# Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function
# and ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.
def ex4():


    n1 = int(input("Enter a number"))
    n2 = int(input("Enter another number"))
    ask = input("add,subtract,multiply, or divide ")
    if ask.lower() == "add":
        print(plus(n1, n2))
    elif ask.lower() == "subtract":
        print(minus(n1, n2))
    elif ask.lower() == "multiply":
        print(times(n1, n2))
    elif ask.lower() == "divide":
        print(division(n1, n2))


if __name__ == '__main__':
    main()
