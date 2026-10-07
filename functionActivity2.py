# problem 1 
# create a function that will take 2 inputs and 
# compare them.
# your inputs should be numbers.
# the function should compare if the first input is less than the second input
# if it is less than the second input it should print true.
# if it is not, it should print false.

def CompareVal():
    Num1= input('First number')
    Num2= input('Second numer')
    print=(Num1 > Num2)

#CompareVal()

def CompareHonorroll():
    Grade1= input('type a number')
    AbsentDays= input('type a number')
    print=(Grade1 > 90  and AbsentDays < 5)

CompareHonorroll()