user_input = int(input("wrrite any number"))

if user_input % 2 == 0:
    print("this is even number")
else :
    print("this is odd number")


for x in range (2 , user_input):
    if user_input % x == 0:
        print(f"{user_input} is not a prime number")
    