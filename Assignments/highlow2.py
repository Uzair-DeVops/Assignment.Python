import random


count = 0
score = 0
condition = True
while condition :
    com_num = random.randint(1, 100)
    user_num = random.randint(1, 100)
    print("Your number:", user_num)
    user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
    if (user_guess == "higher" and user_num > com_num)  or (user_guess == "lower" and user_num < com_num) :
        score += 1
        print("you are correct")
        print("your score is  ", score)
        print("computer number is" , com_num)
    else:
        print("you are wrong")
        print("your score is" , score)
        print("computer number is " , com_num)
    user_input = input("do you want to quite yes or no " ).lower()
    if user_input == "yes":
        condition = False
    else: 
        print("next round")

print("game over you final score is " , score)


