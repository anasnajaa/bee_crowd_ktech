# user input and string concat
name = input('What is your name? ')
print('hi ' + name)

# built-in functions
birth_year = input('Birth Year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

# String array
course = "John's python course"
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:])

course_copy = course[:]

print(course_copy)

# multi-line string
mail = """
Hello
User
"""

print(mail)

# multi-line output

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
num1 = int(num1)
num2 = int(num2)
print(f'''
Results:\n
{num1} * {num2} = {num1 * num2}
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} / {num2} = {num1 / num2}
''')


# String format
first_name = "Anas"
last_name = "Najaa"
message = first_name + " [" + last_name + "]"
message_formatted = f"{first_name} [{last_name}]"
print(message)
print(message_formatted)


# string functions
course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course)

print(course.find('for'))
print(course.find('O'))

print(course.replace('for', 'to'))

# in function
print('Python' in course)
