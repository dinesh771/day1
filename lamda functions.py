# def add_num(a,b):
#     return a+b
# print(add_num(5,5))
# add_num

# with lambda
# def add_num(a,b):
#     return a+b
# add_num= lambda a,b:a+b
# print(add_num(5,5))

# def mult_num(c,d):
#     return c*d
# mult_num=lambda c,d:c*d
# print(mult_num(5,5))

# to convert celisius in to farehelt

# celtofar= lambda c: (9/5)*c+12

# print(celtofar(37))


# evenodd= lambda num: 'even' if num%2==0 else'odd'
# print(evenodd(5))



# lambda functions using sort()

# names=['dinesh','praneeth','gani','jayanth']
# names.sort(key=lambda x:len(x))
# print(names)

# numbers=[20,65,48,798,1,3,5,68]
# numbers.sort(key=lambda num:len(str(num)))
# print(numbers)


# lambda with map() functions
# list1=[1,2,3,4,5,6,7,8,9]
# sqlist=list(map(lambda num:num**3,list1))
# print(sqlist)

# lambda with filter() functions
# list2= [1,2,3,4,5,6,7,8,9,10,12,14,18,20]
# filterfunc=list(filter(lambda num:num%3==0,list2 ))
# print(filterfunc)

# lambda with reduces() functions
from functools import reduce
list3=[1,2,3,4,5]
redfunc=reduce(lambda num1,num2:num1*num2 ,list3)
print(redfunc)