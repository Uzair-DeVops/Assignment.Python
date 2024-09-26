import random

score = 0
count = 0

while count < 3:
    com_num = random.randint(1, 100
    user_num = random.randint(1, 100)
    print("Your number:", user_num)
    user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
    count += 1
    
    if user_guess == "higher":
        if user_num > com_num:
            print("You are correct! the computer number was " , com_num)
            score += 1
        else:
            print("You are wrong, the computer's number is higher." , com_num)
    
    elif user_guess == "lower":
        if user_num < com_num:
            print("You are correct! the computer number was " , com_num)
            score += 1
        else:
            print("You are wrong, the computer's number is lower." , com_num)
    
    else:
        print("Invalid input. Please type 'higher' or 'lower'.")
    
    print(f"Your score is now: {score}")
print(f"\nGame over! Your final score is: {score}")
