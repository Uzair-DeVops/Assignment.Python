# You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. After gathering this information, the program should greet the user with a personalized message that includes their name. The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.



num_list = []
user_name = input("Write your name: ")
print()

# Collect three favorite numbers
for i in range(1, 4):
    num = int(input(f"Enter your {i} favorite number: "))
    num_list.append(num)

# Check if each number is even or odd
print(f"\nHello, {user_name}! Let's explore your favorite numbers:\n")
for num in num_list:
    if num % 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")

# Display each number and its square
print()
for num in num_list:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

# Calculate and display the sum of the numbers
sum_numbers = sum(num_list)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}\n")

# Check if the sum is a prime number
is_prime = True
if sum_numbers <= 1:
    is_prime = False
else:
    for i in range(2, sum_numbers):
        if sum_numbers % i == 0:
            is_prime = False

if is_prime:
    print(f"Wow! The number {sum_numbers} is a prime number!")
else:
    print(f"Great job! The number {sum_numbers} is not a prime number.")
