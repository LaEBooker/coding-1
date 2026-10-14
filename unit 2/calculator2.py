def calcuate_add():
    print("program has started: type inn 2 numbers to add:")
    num1= int(input())
    num2= int(input())
    print(num1 + num2)
    print("program has ended.")

#calcuate_add()

def calcuate_multiply():
    print("program has started: type in 2 numbers to multiply:")
    num1= int(input())
    num2= int(input())
    print(num1 * num2)
    print("program has ended.")

#calcuate_multiply()

def calcuate_sub():
    print("program has started: type in 2 numbers to subtract:")
    num1= int(input())
    num2= int(input())
    print(num1 - num2)
    print("program has ended.")

#calcuate_sub()

def calcuate_divide():
    print("program has started: type in 2 numbers to divide:")
    num1= int(input())
    num2= int(input())
    print(num1 / num2)
    print("program has ended.")

#calcuate_divide()

def mainCalculator():
    print('please tpye a number')
    selection= int(input())
    if selection ==1:
        calcuate_add()
    elif selection ==2:
        calcuate_sub()
    elif selection ==3:
        calcuate_multiply()
    elif selection ==4:
        calcuate_divide()
    else:
        print('sorry something went wrong') 

mainCalculator()