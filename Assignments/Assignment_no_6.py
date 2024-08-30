def even_checker(num):
    if num % 2 == 0:
        return "even"
    else :
        return "odd"
def tuple_1(a , b ):
    list1 : list = [] 
    b = (b)**2
    list1.append(a)
    list1.append(b)
    tu = tuple(list1)
    return tu
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num_list : list = []
user_name : str = input("write your name : ")
print()
for x in range(1,4):
    num = int(input(f"enter your {x} favorite number : "))
    num_list.append(num)
print(f" \n Hello, {user_name} Let's explore your favorite numbers : \n\n The number {num_list[0]} is {even_checker(num_list[0])}  \n The number {num_list[1]} is {even_checker(num_list[1])}  \n The number {num_list[2]} is {even_checker(num_list[2])}")
print()
for x in range (3):
    print(f"The number {num_list[x]} and its square: {tuple_1(num_list[x],num_list[x])} ")
print()
print(f"Amazing! The sum of your favorite numbers is: {sum(num_list)}")
print()
if is_prime(sum(num_list)):
    print(f"Wow! The 1{sum(num_list)} number is a prime number!")
else:
    print(f"Great job! {sum(num_list)} number is not a prime number.")