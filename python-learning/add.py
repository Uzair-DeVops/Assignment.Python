num1  = int(input("write your first num"))
num2  = int(input("write your second num"))
addition = num1 + num2
print(f"The sum of two give numbers is : {addition}")

fvrt_pet =input("what's your favorite animal  : ?  ")
print(f"My favorite animal is also  {fvrt_pet} ")

tem_in_fh = int(input("write tem in fh"))
tem_in_cel = (tem_in_fh - 32) * 5 /9
print(f" tem in fh : {tem_in_fh} \n tem in cel {tem_in_cel}")

side1 = int(input("what is len side1"))
side2 = int(input("what is len side2"))
side3 = int(input("what is len side3"))
perimeter = side1 + side2 + side3
print(f"The perimeter of triangle is : {perimeter}")

numbers = [1,2,3,4,5]
del numbers[2]
print(numbers)

list1 = [1,2,3]
list2 = [4,5,6]
list2.extend(list1)
print(list2)

elements = [10 ,20 ,30 ,40]
elements.pop()
print(f" The pop method without any argument will remove the last element from the list \n and the list will look like this {elements}")


colors = [ "red" ,"blue" ,"green" , "yellow"]
print(f" The index of color yellow is  {colors.index("yellow")}")

def  get_last_element(lst):
    last_item_list = []
    last_item= lst.pop
    last_item_list.append(last_item)
    return last_item_list


user_command = input("press enter to exit")
condition = True
while condition:
    list1 = []
    num = int(input("enter a value")) 
    list1.append(num)
    if user_command == "" :
        condition = False
        print(f"here is list : {list1}")
    


