import sys 

# Size of integer

num : int = 0
size_of_integer = sys.getsizeof(num)
print(f"Size of Integer : {size_of_integer}")

# Size of String 
string : str = ""
size_of_string = sys.getsizeof(string)
print(f"Size of String : {size_of_string}")

# Size of float 
float_num : float = 0.0
size_of_float_num = sys.getsizeof(float_num)
print(f"Size of Float_num : {size_of_float_num}")

# Size of bool
Bol : bool = True
size_of_bool = sys.getsizeof(Bol)
print(f"Size of Boolean : {size_of_bool}")