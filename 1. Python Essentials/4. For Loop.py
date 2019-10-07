## This file contains functions that implments the following tasks using a for loop. 

# 1. Write a program to print 10 even numbers and 10 odd numbers.
# 2. Write a program to find factorial of a number.
# 3. Write a program to generate tables of 10.
# 4. Write a program to add the digits of a number.
# 5. Write a program to reverse the digits of a number.
# 6. Write a program to generate 10 Fibonacci numbers



def for_ten_even_odd():
    '''This function prints first 10 even and odd number using a for loop'''
    evens = [i for i in range(21) if i>0 and i%2 == 0]
    odds = [i for i in range(20) if i%2 != 0]
    print("First 10 even numbers:", evens)
    print("First 10 odd numbers:", odds)    

for_ten_even_odd()



def for_factorial(num):
    '''This function prints the factorial of a number using a for loop'''
    product = 1
    for i in range(num+1):
        if i == 0:
            pass
        else:
            product = product*i
    return product

for_factorial(4)



def for_tables(num):
    '''This function prints multiplication tables of a number using a for loop'''
    for i in range(11):
        if i == 0:
            pass
        else:
            print("{0} x {1} = {2}".format(num, i, num*i))

for_tables(10)



def for_sum_of_digits(num):
    '''This function sum of digits using a for loop'''
    
    sum = 0
    str_num = str(num)
    for i in str_num:
        sum = sum + int(i)
    return sum

for_sum_of_digits(654)



def for_reverse_int(num):
    '''This function prints reverse of a integer using a for loop'''
        
    rev_str = ''
    str_num = str(num)
    last = len(str_num) - 1
    for i in range(len(str_num)):
        rev_str = rev_str + str_num[last - i]
    
    return int(rev_str)
    #return int(str(num)[::-1])

for_reverse_int(987)



def for_fibonacci(num):
    '''This function prints fibonacci series using a for loop'''
    
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(3, num+1):
        # assinging sum to a new variable
        c = a + b
        # swapping two numbers
        a = b
        b = c
        print(c)

for_fibonacci(6)
