
# def add(x, y):
#     """This function adds two numbers."""
#     return x + y

# def subtract(x, y):
#     """This function subtracts two numbers."""
#     return x - y

# def multiply(x, y):
#     """This function multiplies two numbers."""
#     return x * y

# def divide(x, y):
#     """This function divides two numbers and handles division by zero."""
#     if y == 0:
#         return "Error: Division by zero is not allowed."
#     else:
#         return x / y

# def mod(x, y):
#     """This function calculates the modulus of two numbers."""
#     if y == 0:
#         return "Error: Division by zero is not allowed."
#     return x % y

# def exponent(x, y):
#     """This function raises x to the power of y."""
#     return x ** y


# first_value = int(input( "write your first number : "))
# second_value = int(input( "write your second number : "))
# choice = input("choice what do you want to do : ( '+ , - , * , / , % , **'  ) : ")
# if choice == "+":
#     print(add(first_value,second_value))
# elif choice == "*":
#     print(multiply(first_value , second_value))
# elif choice == "-":
#     print(subtract(first_value, second_value))
# elif choice == "/":
#     print(divide(first_value, second_value))
# elif choice == "%":
#     print(mod(first_value, second_value))
# elif choice == "**":
#     print(exponent(first_value, second_value))
# else :
#     print("invalid choice")

    





















def databas():
    student_list = []
    mini_list = []
    condition = True
    Id = 1
    while condition:
        user_input = input ("Please enter the student's name (or type 'stop' to finish) : ")
        if user_input.lower() == "stop":
            condition = False
        else:
            mini_list = []
            mini_list.append(Id)
            Id += 1
            mini_list.append(user_input)
            tuple1 = tuple(mini_list)
            student_list.append(tuple1)
print(student_list)
print()
print("List of Students with IDs:")
for items in student_list:

      print (f"ID: {items[0]}, Name: {items[1]}")

print()
# print(sum(student_list))
total = 0
for items in student_list:
      total +=  1
print(f"Total number of students  : {total}")

length = 0
for items in student_list:
     length +=   len(items[1])

print(f"Total length of all student names combined: {length}")


longest_name_student = student_list[1]  # Start with the first student

for student in student_list:
    if len(student[1]) > len(longest_name_student[1]):
        longest_name_student = student

print(f"The student with the longest name is: {longest_name_student[1]}")


shortest_name_student = student_list[1]  # Start with the first student

for student in student_list:
    if len(student[1]) < len(shortest_name_student[1]):
        shortest_name_student = student

print(f"The student with the shorted  name is: {longest_name_student[1]}")

