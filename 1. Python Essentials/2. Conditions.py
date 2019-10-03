# 1. Write a program to check if a candidate is eligible for voting or not.
# 2. Write a program to check if the number is positive or negative.
# 3. Extend the previous program to check whether the given number is positive, zero or negative. 

class A(object):
    def vote_eligibility(age):
        if age > 18:
            print("Eligible to vote")
        else:
            print("Not eligible to vote")
        
    def positive_negative(number):
        if number < 0:
            print("Negative number")
        elif number > 0:
            print("Positive number")
        else:
            print("Neither positive nor negative")
            

class B(A):
    # num = 10
    positive_negative(num)
    
b = B()
b.positive_negative(10)
