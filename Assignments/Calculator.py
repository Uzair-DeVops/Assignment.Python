first_value = int(input( "write your first number : "))
second_value = int(input( "write your second number : "))
choice = input("choice what do you want to do :  '+ , - , * , /'")
if choice == "+":
    print(first_value + second_value)
elif choice == "*":
    print(first_value * second_value)
elif choice == "-":
    print(first_value - second_value)
elif choice == "/":
    print(first_value / second_value)
else :
    print("invalid choice")

    