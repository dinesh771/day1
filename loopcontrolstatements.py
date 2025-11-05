# for i in range(1,5):
#     if i%0!=0:
#         continue
#     print(i)


# for i in range(5):
#     num = int(input("Enter a number: "))
#     if num < 0:
#         continue  
#     print("Positive number:", num)

# list1=[]
# for i in range(-5,5):
#    # num=int(input('enter a number:'))
#     if i<=0:
#         continue
#     list1+=[i]
# for i in list1:
#     print(i)

list1 = ['mon','tue','wed','thur','fri','sat','sun']
weekends = ['sat','sun']
workingdays = []

for day in list1:   # fixed here
    if day in weekends:
        continue
    workingdays += [day]
    print(workingdays)

