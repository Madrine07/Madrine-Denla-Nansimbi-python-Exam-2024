
student_name = input("Enter student name: ")
student_number = input("Enter the student number: ")
programming = int(input("Enter the programming mark: "))
data_science = int(input("Enter the data science mark: "))
computer_applications = int(input("Enter the computer applications mark: "))
total_marks = programming + data_science + computer_applications
total_subjects = 3
average_mark = total_marks / total_subjects
print(f"The average mark of {student_name} with a student number of {student_number} is: {average_mark:.3f}")


# 2) ii)
def car_miles_per_gallon_used():
   milesDriven = int(input("Enter the number of miles driven: "))
   gallonsOfGasUsed = int(input("Enter gallons used: "))
   mpg = milesDriven / gallonsOfGasUsed
   print(f"The car's miles per gallon used are: {mpg:.3f} ")
car_miles_per_gallon_used()


# 2) iii)
def odd_numbers_between_one_and_one_hundred():
     for number in range(1,101):
         if number % 2 != 0:
             print (number)
odd_numbers_between_one_and_one_hundred()


