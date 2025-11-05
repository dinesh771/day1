# def add_num():
#     num1=int(input('enter a number:'))
#     num2=int(input('enter a number:'))
#     print(num1+num2)

# print('this is firt code')
# add_num()


# def greet(name, ok):
#     print(f'''     hello {name}, 
#              welcome to {ok} class''')

# greet('dinesh', 'python')

# def greet1(): #function declaration without defining it.
#     pass



def check_loan(income, credit):
    if income >= 25000 and credit >= 700:
        print("Eligible for loan")
    elif income < 25000 and credit < 700:
        print("Improve your score and increase income to become eligible")
    else:
        print("Not eligible for loan")

check_loan(2000, 450)
check_loan(15000,500)

