# # my_functions.py
# def greet():
#     print("Hey")

# greet() # ADDED

# # => Hey

# #Let's return it now!
# def greet_again():
#     return "Hey you"

# greeting = greet_again() # ADDED
# print(greeting)
# # => Hey

# def hello(name):
#     return "Hey " + name

# rita = hello("Rita")

# print(rita)


# def hello_time(name, time_of_day):
#     return "Good " + time_of_day + ", " + name

# gutentag = hello_time("Rita", "morning")
# print(gutentag)

# chosen = "Rita"


#Scope
def greet():
    words = "Yo"
    return words

# def greet_2():
#     return words
# print(greet_2())
#This doesn't work because words is not defined within greet2(). Scope is local within a function. I think.

bye = "l8r"

def greet_3():
    return bye
print(greet_3())
#This works because bye was defined outside of the function. It has a GLOBAL scope.