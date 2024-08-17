# Global variable
x = 10

def my_function():
    # Local variable
    y = 5
    print("Inside the function, x (global):", x)
    print("Inside the function, y (local):", y)

# Calling the function
my_function()

# Accessing the global variable outside the function
print("Outside the function, x (global):", x)

# Trying to access the local variable outside the function will cause an error
# print("Outside the function, y (local):", y) 
