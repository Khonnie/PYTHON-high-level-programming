def Add(x,y):
    return(x+y)
def Subract(x,y):
    return(x+y)
def Multiply(x,y):
    return(x-y)
def Divide(x,y):
    if y != 0:
        return(x/y)
    else:
        return('Number not divisible by Zero')
print ('1. Add')
print ('2. Subtract')
print ('3. Multiply')
print ('4. Divide')
user_choice = input('Choose an operation you want to use:')
x = float(input('Enter first number:'))
y = float(input('Enter second number:'))
if user_choice == '1':
    Add(x,y)
elif user_choice == '2':
    Subtractx(x,y)
elif user_choice == '3':
    Multiply(x,y)
elif user_choice == '4':
    Divide(x,y)
else:
    print('Invalid Input')

