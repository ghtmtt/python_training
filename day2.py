r = range(1, 100)
# print(r)

l = list(r)
# print(l)

# d = {'a': [1,2,3,.....50], 'b': [1,2, 3.... 20]}


# if the key is 'a' print values > 25 if not print(no values)
# if the key is 'b' print values < 10 if not dont do anything

ra = list(range(1,50))
rb = list(range(1,20))
d = {'a': ra, 'b': rb}
d = {'a' : list(range(1,50)), 'b': list(range(1,20))}
# print(d)



# for k, v in d.items():
#     if k == 'a':
#         for i in v:
#             if i > 25:
#                 print(i)
#             else:
#                 print('no values')
#     if k == 'b':
#         for i in v:
#             if i < 10:
#                 print(i)

# print(d['a'])

l = []

for i in d['a']:
    if i > 25:
        l.append(i)




def my_function():
    '''
    This function prints something
    This function does not need parameters
    '''
    print("Hi Python")


# my_function()
my_function

# print(help(my_function))

def my_function2(s):
    print(s)

# my_function2('Matteo')

# name = 'my Matteo'

# def my_function3(name='Matteo', age):
#     print(name, age)

# print(name)
# my_function3('John', 45)

def multiply(x, y):
    result = x * y
    print(result)

# multiply(10, 35)


l = [10, 2, 3, 50]

def multiply2(*args):
    v = 1

    for i in args:
        v = v * i
    
    return v

# multiply2(1,30, 90, 4, 3)
mynumber = multiply2(*l)
# print(mynumber)






def rect_area(width, height):

    calculation = width * height

    return calculation

my_area = rect_area(100, 40)
# print(my_area)




def shape_area(shape, width, height):

    if shape == 'rectangle':

        calculation = width * height
    
    if shape == 'triangle':

        calculation = width + height / 2
    
    else:
        print('I do not know the shape')
        
    return calculation

area = shape_area('triangle', 100, 5)
# print(area)


# fahrenheit = (celsius * 9 / 5) + 32


def fahrenheit(celsius):

    f = (celsius * 9 / 5) + 32
    return f

a = fahrenheit(100)





def fahrenheit2(*args):

    lf = []

    for c in args:

        calculation = (c * 9 / 5) + 32
        lf.append(calculation)
    
    return lf


lc = [10, 0, 100, 50]
my_f = fahrenheit2(10, 0, 90, 33, 2, 45, 12)
my_f2 = fahrenheit2(10, 0, 90, 33, 2, 45, 12)

print(my_f)
print(my_f2)









































