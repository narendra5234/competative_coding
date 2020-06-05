# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
# print(greet_bob(be_awesome))
# -----------------------------------------------------------------------------
# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
#
#
#
# print(parent())
# ------------------------------------------------------------------------------
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# print(parent(1))
# -------------------------------------------------------------------------------

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     if num == 1:
#         return first_child

# print(parent(1)())

def my_decorator(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        func(name)
        print("Something is happening after the function is called.")
    return wrapper


# def say_whee():
#     print("Whee!")
# print(my_decorator(say_whee))




@my_decorator
def say_whee(name):
    print(name)

print(say_whee("narendra"))
# print(my_decorator(say_whee)())