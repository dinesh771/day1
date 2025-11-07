# # Define a function that takes a list of numbers as a parameter
# def sum_of_digits(numbers):
#     # The sum() function returns the total of all elements in the list
#     return sum(numbers)

# # List of digits
# digits_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Call the function and store the result
# result = sum_of_digits(digits_list)

# # Print the result
# print("The sum of all digits in the list is:", result)



# str1 = 'hsenid'  # Given string
# rev = ''         # Initialize an empty string to store the reversed string

# # Loop through each character in the original string
# for char in str1:
#     rev = char + rev  # Add the current character to the beginning of 'rev'

# # Print the reversed string
# print(rev)

list1=['hsenid ', 'luap ', 'inag ', 'ayaj ', 'ayad ']
list2=[ ]
for words in list1:
    rev = ' '
    for char in words:
      rev = char + rev
    list2.append(rev)
print(list2)

