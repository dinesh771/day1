# a=15
# b=20
# if a>b:
#     print('A is greater')
# else:
#     print('B is greater')

# result='A is greater' if a>b else 'B is greater'
# print(result)

# def category(age):
#     return 'major' if age>18 else 'minor'
# print(category(21))
# print(category(16))


# def evenodd(num):
#     return 'even' if num%2 == 0 else'odd'
#     print(evenodd(5))

# list1=[1,2,3,4,5,6,7,8,9,10]
# evenodd=['even' if n%2==0 else'odd' for n in list1]
# print(evenodd)

# list2 = ['dinesh', 'jaswanth', 'jaya']
# length = [len(item) for item in list2]
# print(length)

# salary = int(input('enter a number: '))
# if salary>150000:
#     print('you are eligible for pelli chupulo')
# else:
#     print('you are not eligible for pelli ')

# num = int(input('enter a number: '))

# result= 'positive' if num>0 else 'negative' if num<0 else 'zero'
# print(result)

# mark = int(input('Enter marks: '))
# result = 'pass' if mark > 50 else 'fail' if mark < 50 else ''
# print(result)

def good_morning():
    return 'Hello good morning'

def good_afternoon():
    return 'hi good afternoon'

def  good_evening():
    return 'evening evening'
def good_night():
    return 'good night'
time = int(input('enter  time in the format of 24hours: '))
greetings= good_morning() if time <12 else good_afternoon() if time <17 else good_evening() if time<21 else 'good night'
print(greetings)