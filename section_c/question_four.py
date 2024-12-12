# 4) i) a)
# Object-Oriented Programming (OOP) is a programming model 
# that uses objects to represent data and actions.
# helps developers create robust, maintainable, and scalable applications. 

# 4) i) b)
# In object-oriented programming (OOP), a class is a template for 
# creating objects whereas an object is an instance of a class.

# 4) ii)
def word_count():
    sentence = "python exam"
    words = sentence.split()
    word_count = {} 
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)
word_count()

# 4) iii)
def sum_of_two_numbers(a, b):
     return a + b
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

sum_of_two_numbers(3, 4)
print("The sum of the two numbers a and b is {0}".format(sum_of_two_numbers(a , b)))

# 4) iv) AND 4) V)
class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

    def start_engine(self):
         print(f"The engine of the {self.brand}, {self.name} of color {self.color} has started.")

my_car = Car('Jaguar Land Rover',"Range Rover", "Golden")
print(f"My car brand is: {my_car.brand}")
print(f"My car name is: {my_car.name}")
print(f"My car color is: {my_car.color}")

my_car.start_engine()


