## This file contains functions that implments the following tasks using a for loop. 

# 1. Write a program to print 10 even numbers and 10 odd numbers.
# 2. Write a program to find factorial of a number.
# 3. Write a program to generate tables of 10.
# 4. Write a program to add the digits of a number.
# 5. Write a program to reverse the digits of a number.
# 6. Write a program to generate 10 Fibonacci numbers


def while_even_odd(condition):
    '''This function prints first 10 even and odd number using a while loop'''
    
    num = 1
    while(num < 21):
        if condition == 'even':
            if num % 2 == 0:
                print(num)
        elif condition == 'odd':
            if num % 2 != 0:
                print(num)
        num = num + 1

while_even_odd('even')



def while_factorial(num):
    '''This function prints the factorial of a number using a while loop'''

    product = 1
    count = 1
    while(num < count):
        product = product * i
        count = count + 1
    return product

while_factorial(5)



def while_tables(num):
    '''This function prints multiplication tables of a number using a while loop'''
    
    count = 1
    while(count < 11):
        print("{0} x {1} = {2}".format(num, count, num*count))
        count = count + 1

while_tables(10)



def while_sum_of_digits(num):
    '''This function sum of digits using a while loop'''

    str_num = str(num)
    i = 0
    sum = 0
    while i < len(str_num):
        sum = sum + int(str_num[i])
        i = i + 1
        
    return sum

def while_sum_of_digits(num):
    '''This function returns sum of digits using a while loop '''
    
    sum = 0
    while(num):
        sum = sum + num%10
        num = num//10
    return sum

while_sum_of_digits(10)



def while_reverse_int(num):
    '''This function prints reverse of a integer using a while loop'''
    
    rev_str = ''
    str_num = str(num)
    last = len(str_num) - 1
    i = 0
    while last >= 0:
        rev_str = rev_str + str_num[last]
        last = last - 1
    
    return int(rev_str)

while_reverse_int(199)



def while_fibonacci(num):
    '''This function prints fibonacci series using a while loop'''

    a = 0
    b = 1
    print(a)
    print(b)
    
    count = 3
    while count <= num:
        c = a + b
        a = b
        b = c
        print(c)
        count = count + 1

while_fibonacci(6)
