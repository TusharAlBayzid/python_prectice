'''
# Functions 



def say_bye():
    print("hahahaha 😂")

def say_hello():
    print("Hi")
    print("Hello")
    print("Bye")
    say_bye()
    print("👿")

print("ki obosta ra")
say_bye()
say_hello() 


def find_area(radius):
    area = 3.14159 * (radius ** 2)
    print(area)

find_area(10)

def square(number):
    result = number * number
    return result

output = square(5)
print(output)


def calc_area(r):
    return 3.14159 * r ** 2

print(calc_area(5))


lambda r: 3.14159 * r ** 2 

print(calc_area(6))



# Decorator

def add_cream(func):
    def wrapper():
        print("Making Special Cream Food!")
        func()
        print("Add cream on top!")
    return wrapper

@add_cream
def make_coffee():
    print("Making Plain Coffee")
    print("okay")
    
@add_cream
def make_cake():
    print("making tea")
    

make_coffee()
make_cake()


# Decorator

def store_decorator(func):
    def wrapper(*args, **kwargs):
        print("Welcome to Pet Paradise")
        func(*args, **kwargs)
        print("Thnak you for Shopping")
    return wrapper


@store_decorator
def buy_pet(pet_name):
    print(f"You bought {pet_name}!")

buy_pet("Fluffy")

'''

def fruits():
    yield "apple"
    yield "banana"
    yield "cherry"
    
fruit_iterator = iter(fruits())

print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))

