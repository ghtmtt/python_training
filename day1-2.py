s = 'john'

m = 10

# print(dir(s))

s = s.upper()

l = [1,2,3,4,5]
# print(dir(l))
# print(help(l.append))
l.append(100)
# print(l)

l = [2, 1, 4, 79, 3, 100, 50]
l.sort(reverse=True)
# print(l)


d = {'Italy': 'Rome', 'Germany': 'Berlin', 'Spain': 'Madrid'}
# print(d)
# print(dir(d))
# print(help(d.keys))
# print(d.keys())
# print(d.values())
# print(d.items())


# loops

l = [1,2,3,4,5,6,7,8,9,10]

# for i in l:
#     print(i)


l1 = [10, 20, 30, 40, 50, 60]
l2 = ['A', 'B', 'C', 'D']
lt = [l1, l2]

# for i in lt:
#     print(i)


# for i in lt:
#     for j in i:
#         print(j)
#     print(i)

# for i, j in enumerate(l1):
#     print(i, j)

val = 0

# while val <= 20:
#     print(val)
#     # val = val + 2
#     val += 2


# for i in l:
    # pass

d = {'names': ['John', 'Maria', 'Anna'], 'age': [21, 25, 13]}

# for k, v in d.items():
#     if k == 'names':
#         for i in v:
#             print(i)
#     else:
#         print('I dont know what to do')




# for k in d.keys():
#     print(k)

# for v in d.values():
#     print(v)

# for k, v in d.items():
#     print(k, v)


l1 = [10, 20, 30, 40, 50, 60]


# if len(l1) < 5:
#     print('I am a long list')
# elif len(l1) == 6:
#     print('I am 6 long')
# else:
#     print('I am inside the else')


i = 10
o = 0

try:
    result = i / o
except ZeroDivisionError as e:
    print('I cannot divide by 0', e)

l1 = [1,2,3]
print(l1)









