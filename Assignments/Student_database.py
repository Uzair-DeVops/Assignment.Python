def list_students_with_ids(student_list):
    print("\nList of Students with IDs:")
    for items in student_list:
        print(f"ID: {items[0]}, Name: {items[1]}")

def find_longest_name(student_list):
    longest_name_student = student_list[0]  
    for student in student_list:
        if len(student[1]) > len(longest_name_student[1]):
            longest_name_student = student
    print(f"The student with the longest name is: {longest_name_student[1]}")

def find_shortest_name(student_list):
    shortest_name_student = student_list[0]  
    for student in student_list:
        if len(student[1]) < len(shortest_name_student[1]):
            shortest_name_student = student
    print(f"The student with the shortest name is: {shortest_name_student[1]}")

def total_name_length(student_list):
    length = 0
    for items in student_list:
        length += len(items[1])
    print(f"Total length of all student names combined: {length}")

def check_student_exists(student_list, name):
    for student in student_list:
        if student[1].lower() == name.lower():  
            print(f"Student name '{name}' already exists.")
            return True
    return False

def total_number_of_students(student_list):
    total = 0
    for x in student_list:  
        total += 1
    print(f"Total number of students: {total}")

def manage_student_database():
    student_list = []
    mini_list = []
    condition = True
    Id = 1
    while condition:
        user_input = input("Please enter the student's name (or type 'stop' to finish): ")
        if user_input.lower() == "stop":
            condition = False
        else:
            if check_student_exists(student_list, user_input):
                continue
            
            mini_list = []
            mini_list.append(Id)
            Id += 1
            mini_list.append(user_input)
            tuple1 = tuple(mini_list)
            student_list.append(tuple1)

    print()
    list_students_with_ids(student_list)
    print()
    total_number_of_students(student_list) 
    print()
    total_name_length(student_list)  
    print()
    find_longest_name(student_list)
    print()
    find_shortest_name(student_list)

manage_student_database()


