# 1. Write a program to find largest of two numbers.
# 2. Write a program to check given number is even or odd. (Hint: use % operator)

def largest(num1, num2):
    if num1 > num2:
        print("First number is larger")
    elif num1 < num2:
        print("Second number is larger")
    else:
        print("Numbers are equal")
        
largest(10, 20)

def even_odd(number):
    if number == 0:
        print("Number is neither even nor odd")
    else:
        if number % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

even_odd(0)
