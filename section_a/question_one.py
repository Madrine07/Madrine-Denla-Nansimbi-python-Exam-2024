# i)
def calculate_area (circle_radius):
    
    if(circle_radius > 0):
         pie = 3.14
         result = pie * (circle_radius)**2
         print(result)
    else:
         result = 0
    return result

print('The area of the circle is: ')
calculate_area (4)


# ii)
#integers = [4,7,2,9,12,15]
def odd_numbers():
    
    integers = [4,7,2,9,12,15]
    sum = 0
    for int in integers:
        if int % 2 != 0:
            sum += int
    print(f"The sum of all odd numbers in the list of integers is: {sum}")
    
odd_numbers()

# iii)
def python_function():
    
    num_one = int(input('Enter any given number: '))
    num_two = int(input('Enter any given number: '))
    sum = num_one + num_two
    difference = num_one - num_two
    product = num_one * num_two
    quotient = num_one / num_two
    print(f"The sum, difference, product and quotient of num one and num two is: {sum}, {difference}, {product} and {quotient} respectively.")
    
python_function()

# iv)
student_info = {
    'name': 'Alice',
    'age' : 20,
    'grade': 'A'
}
student_info ['age'] = 26
student_info ['city'] = 'New Kampala'
print(student_info)
    


