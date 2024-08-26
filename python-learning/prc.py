user_command = input("type enter to exit")
condition = True
while condition:
    list1 = []
    num = int(input("enter a value")) 
    list1.append(num)
    if user_command == "enter" :
        condition = False
print(f"here is list : {list1}")