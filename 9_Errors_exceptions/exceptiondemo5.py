 
#print more dynamic exception message text
try:
    a = float(input('First number, please: '))
    b = float(input('Second number: '))
    print('Your result is ', a/b)
except (ZeroDivisionError, ValueError, TypeError) as e:
    print('Error: ', e)
 
