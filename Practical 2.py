
# Q: Write a program to find area and perimeter of geometric objects
obj = input("Enter the shape of object (circle/square/triangle/rectangle)")
if obj == 'circle':
  r = int(input("Enter the radius of a circle: "))
  print("The area of a circle is ", 3.14 * r * r)
  print("The circumference of a circle is ", 2 * 3.14 * r)
elif obj == 'square':
  s = int(input("Enter the side of a square: "))
  print("The area of a square is ", a * a)
  print("The perimeter of a square is ", 4 * a)
elif obj == 'triangle':
  b = int(input("Enter the base of a triangle: "))
  h = int(input("Enter the height of a triangle: "))
  s1 = int(input("Enter the side 1 of a triangle: "))
  s2 = int(input("Enter the side 2 of a triangle: "))
  print("The area of a triangle is ", (h * b) / 2)
  print("The perimeter of a triangle is ", s1 + S2 + b)
elif obj == 'rectangle':
  l = int(input("Enter the length of a rectangle: "))
  b = int(input("Enter the breadth of a rectangle: "))
  print("The area of a rectangle is ", l * b)
  print("The perimeter of a square is ", 2 (l * b))
else:
  print("Enter the valid shape!")
  

# Q: The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in metres, feets, inches and centimetres
km = int(input("Enter the disance between two cities in kms: ")) 
unit = input("Enter the unit for conversion (metres/feet/inches/centimetres): ")
if unit == 'metres':
  print("The distance in metres: ", km * 1000)
elif unit == 'feets':
  print("The distance in feets: ", km * 3281)
elif unit == 'inches':
  print("The distance in inches: ", km * 39370)
elif unit == 'centimetres':
  print("The distance in centimetres: ", km * 100000)
else:
    print("Enter the valid unit!")


  

# Q: Write a program to interchange two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("Interchanged numbers are as follows \n First number: ", a, "\n Second number: ", b)


# Q: Write a program to compute Fahrenheit from centigrade (f = 1.8 * c + 32)
c = int(input("Enter the temperature in Centigrade: "))
f = (1.8 * c) + 32
print("Temperature in Fahrenheit: ", f )


# Q: Create a datatype identifier
a = 5
print("type of a:", type(a))
b = 5.0
print("type of b:", type(b))
c = 2 + 4j
print("type of c:", type(c))
d ='Name'
print("type of d:", type(d))
e = [2, 4, 4.5, "ABC"]
print("type of e:", type(e))
f = (4, 7.4, 'abc')
print("type of f:", type(f))

# Q:Print whether the number is positive, negative or zero
def number():
    num = int(input("Enter the number:"))
    if num > 0:
        print("The entered number is positive!")
    elif num < 0:
        print("The entered number is negative!")
    elif num == 0:
        print("The entered number is zero!")
        
number()
number()
number()

# Q: Write a program to input the basic salary of an employee and calculate the gross salary according to the given conditions:
# Basic Salary <= 10000: HRA=20% DA=80%
# Basic Salary is between 10001 to 20000: HRA=25% DA=90% 
# Basic Salary >= 20001: HRA=10% DA=95%

# Q: If the ages of three brothers are input through the keyboard, write a program to determine the youngest and oldest of three brothers

# Q: Write a program to calculate the overtime pay of employee, overtime is paid at the rate of Rs.12.00/hour for every hour worked above 40 hours. Assume that employee do not work for fractional hours

# Q: 
