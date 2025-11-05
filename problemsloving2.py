# def add_num():
#     num1=int(input('enter a number:'))
#     num2=int(input('enter a number:'))
#     print(num1+num2)
#     print(num1*num2)
#     print(num1-num2)
#     print(num1%num2)
#     print(num1//num2)
# add_num()

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print("Factorial:", fact)

# num = int(input("Enter a number: "))
# factorial(num)

# def fibonacci():
#     a, b = 0,1
#     for i in range(5):
#         print(a)
#         a, b = b, a + b

# fibonacci()



# def perfect(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     if sum == n:
#         print(n, "is a Perfect Number")
#     else:
#         print(n, "is not a Perfect Number")

# num = int(input("Enter a number: "))
# perfect(num)

num = int(input('enter a number:'))
for i in range(2,num):
    if num%i==0:
        print(f'{num} is not a prime number')
        break
else:
    print(f'{num} is a prime number')


























































































































































































































