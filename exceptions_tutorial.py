# # Errors (syntax error) and exceptions

# #syntax errors
# a = 5 print(a)
# print("hello"))

# #exceptions
# a = 5 + "10" #type error
# import modulethatdoesntexist #module error
# a = 8
# b = c #name error
# f = open('somefile.txt') #file not found error
# a = [1, 2, 3]
# a.remove(5) #value error (5 not in list)
# a[5] #index error
# my_dict = {'neme': 'max'}
# my_dict['age'] #key error

#raising exceptions: forcing an exception to occur when a certain condition is met
try:
    a = 5 / 1
    b = a + 'hello'
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f'an error happened: {e}')
else:
    print('no errors occured')
finally:
    print("this runs always and is used for clean up operations")

#creating our own error classes
class ValueTooHighError(Exception):
    def __init__(self,message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high', x)
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e.message, e.value)

#another example
x = -5
if x<0:
    raise Exception('x should be positve')
#assertion will raise an assert eroor with the below message
assert (x<0), 'x is negative'