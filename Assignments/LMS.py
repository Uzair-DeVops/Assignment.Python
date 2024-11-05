
# books_list = []
# def add_books(id,title,Author,Genre,Status= "Availability"):
#     Items = {"id" : id  , "title" : title ,"Author" :Author ,"Genre" : Genre , "Status" :Status} 
#     books_list.append(Items)
#     return books_list
# add_books(1  ,"Harry Potter" ,"Irtiza" , "Magical"  )
# add_books(2 ,"Chem" ,"Ali" , "sci" , "checkout")
# add_books(3  ,"Phy" ,"Uzair" , "sci"  )

# user_list = []
# def user(id,name,borrow):
#     Items = {"id" : id  , "name" : name ,"borrow" :[borrow]} 
#     user_list.append(Items)
#     return user_list

# user(1  ,"Uzair" , "Harry Potter")
# user(2,"uzair","chem")

# print(books_list)
# print(user_list)

books_list = []

def add_books(**a):
    books_list.append(a)
    return books_list

add_books(id=1, title="Harry Potter", Author="Irtiza", Genre="Magical")
add_books(id=2, title="Chem", Author="Ali", Genre="sci")
add_books(id=3, title="Phy", Author="Uzair", Genre="sci")

user_list = []
def user(**a):
    user_list.append(a)
    return user_list

user(id=1, name="Uzair", borrow=["Harry Potter"])
user(id=2, name="Uzair", borrow=["Chem"])
print(user_list)

print(books_list)



def borrow()



    
# # item = {"id" : 1  , "title" : "Harry Potter" ,"Author" : "Irtiza" ,"Genre" : "Magical" , "Status" : "Availability"} 

# books.append(item)
# print(books)