
# Exploring Favorite Numbers

This code allows users to interactively explore their favorite numbers by checking if they're even or odd, squaring them, summing them, and determining if the sum is a prime number.

## Steps in the Code

### 1. **Defining the `even_checker` Function**
```python
def even_checker(num):
    if num % 2 == 0:
        return "even"
    else :
        return "odd"
```
- **Purpose**: This function checks whether a given number is even or odd.
- **Logic**: 
  - If the number is divisible by 2 (`num % 2 == 0`), it is labeled as "even."
  - Otherwise, it is labeled as "odd."

### 2. **Defining the `tuple_1` Function**
```python
def tuple_1(a, b):
    list1: list = [] 
    b = (b)**2
    list1.append(a)
    list1.append(b)
    tu = tuple(list1)
    return tu
```
- **Purpose**: This function takes two numbers, squares the second number, and returns both as a tuple.
- **Steps**:
  - An empty list `list1` is created.
  - The second input `b` is squared.
  - Both `a` and the squared `b` are added to the list.
  - The list is converted into a tuple and returned.

### 3. **Defining the `is_prime` Function**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
- **Purpose**: This function checks if a given number is prime.
- **Logic**:
  - Numbers less than or equal to 1 are not prime.
  - The function loops from 2 to the square root of `n` to check for factors.
  - If any factor is found, `n` is not prime; otherwise, it is.

### 4. **User Interaction**
```python
user_name: str = input("write your name : ")
```
- **Purpose**: To capture the user's name for personalized output.

### 5. **Collecting Favorite Numbers**
```python
num_list: list = []
for x in range(1, 4):
    num = int(input(f"enter your {x} favorite number : "))
    num_list.append(num)
```
- **Purpose**: To gather three favorite numbers from the user and store them in a list.

### 6. **Displaying Even/Odd Information**
```python
print(f"Hello, {user_name} Let's explore your favorite numbers:
")
for x in range(3):
    print(f"The number {num_list[x]} is {even_checker(num_list[x])}")
```
- **Purpose**: To inform the user whether each of their favorite numbers is even or odd.

### 7. **Displaying Numbers and Their Squares**
```python
for x in range(3):
    print(f"The number {num_list[x]} and its square: {tuple_1(num_list[x], num_list[x])}")
```
- **Purpose**: To display each favorite number along with its square.

### 8. **Summing the Favorite Numbers**
```python
print(f"Amazing! The sum of your favorite numbers is: {sum(num_list)}")
```
- **Purpose**: To calculate and display the sum of the favorite numbers.

### 9. **Prime Check on Sum**
```python
if is_prime(sum(num_list)):
    print(f"Wow! The {sum(num_list)} number is a prime number!")
else:
    print(f"Great job! {sum(num_list)} number is not a prime number.")
```
- **Purpose**: To check if the sum of the favorite numbers is a prime number and inform the user accordingly.
