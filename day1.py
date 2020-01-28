# this is my comment


# integers 
i = 10
# print(i)

ii = int(1.2)
# print(ii)

# floating
f = 1.4
# print(f)

ii = i - f
# print(result)

# strings

s = 'my string'
ss = "my other string"

# print(s, ss)

# i = int(10)

s = 'backslash \\'
# print(s)

s = 'Bob\'s cat'
# print(s)

s = "Bob's cat and Alice's dog"
# print(s)

s = ''' my string\ ' " '''

s = 'My name is \n Matteo'
# print(s)



name = 'Matteo'
complete_name = 'My name is %s' % name
# print(complete_name)

complete_name = 'My name is {}'.format(name)
# print(complete_name)

complete_name = f'My name is {name}'
# print(complete_name)

name = 'Matteo'
surname = 'Ghetta'
age = 33

information = f'''My complete name is {name} {surname} and I'm {age} old'''
# print(information)

mybool = True
mybool2 = False

# print(mybool, mybool2)

i = 1
# print(str(i))

s = '1'
conv = int(s)

# s = 'False'
# print(bool(s))

# print(type(i))

i = 10
ii = 3.0
# print(i/ii)


# lists
l = [1, 2, 3, 4, 5]
# print(type(l))
# print(l)

ll = [1, 'A', 1.2, True]
# print(ll)

# print(l != ll)

l1 = [1,2,3,1,1,1,1,2,2,3,3,3,3,3,3]
# print(l1)

s1 = set(l1)
# print(s1)
# print(type(s1))

lclean = list(s1)
# print(lclean)
# print(type(lclean))

# print(l1[0])

l1[0] = 'A'

# print(l1[-1])
# print(l1[0:3])
# print(l1, len(l1))

l = [1,2,3,4,5,6,7,8,9,10]
# print(l[0])
# print(l[-1])
# print(l[0:3])

# print(l[:-2])

# print(l[11])

l1 = [1,2,3]
l2 = [4,5,6]
lt = l1 + l2
# print(lt)

ltt = l1 * 4
# print(ltt)

lm = [l1, l2]
# print(lm)

# print(lm[0][1])

del lm[0]
# print(lm)

# tuple
t = (1, 2, 3)
# print(t)
# print(type(t))


# dictionaries

d = {'name':'Matteo', 'age': 'Matteo'}
# print(d)

d['name'] = 'Marco'

# print(d['name'])


d = {'names':['Joe', 'Matteo', 'John']}
print(d['names'][0])

d = {'names': ['Joe', 'Matteo', 'John'], 'number':30, 'string': 'I am a string'}
print(d)































