# def rectangle(length=10, breadth=5):
#     area = length * breadth
#     perimeter = 2 * (length + breadth)
#     print("Area of Rectangle:", area)
#     print("Perimeter of Rectangle:", perimeter)

# rectangle()

# rectangle(12, 8)


# def addition(*numbers):
#     total=0     
#     for num in numbers:
#         total+=num

#     print(total)

# addition(10, 20)
# addition(5, 15, 25, 35,3)
# addition()


# def multiplication(*numbers):
#     if not numbers:  
#         print("No numbers to multiply. Result is 0.")
#         return
    
#     result = 1
#     for num in numbers:
#         result *= num
    
#     print("The product is:", result)

# multiplication(2, 3, 4)
# multiplication(5, 10)
# multiplication()  


# def details(values): 
#     for k, v in values.items():
#         print(f"{k}: {v}")

# person = {'name': 'dinesh', 'age': 21, 'place': 'vikrabad'}
# details(person)  



def student_result(**marks):
    total_marks = sum(marks.values())  
    num_subjects = len(marks)          
    percentage = (total_marks / (num_subjects * 100)) * 100  
    
    print("Marks obtained in each subject:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    
    print(f"\nTotal Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")

student_result(Math=100, Physics=100, Chemistry=100, English=100)




 
