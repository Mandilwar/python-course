# print function
print("Hello World")

# Adding a seperator in between of the statements
print("Good Morning", "Umang", sep="-")
name = "Umang"
age = 25
print(f"Hello {name}, you are {age} years old")
# Format function usage
print("Hello {}, you are {} years old".format(name, age))

student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"
stu1_marks = 90
stu2_marks = 87
stu3_marks = 95
print("Student 1: {} scored {} marks, Student 2: {} scored {} marks, Student 3: {} scored {} marks".format(student1, stu1_marks, student2, stu2_marks, student3, stu3_marks))
print(f"Student 1: {student1} scored {stu1_marks} marks, Student 2: {student2} scored {stu2_marks} marks, Student 3: {student3} scored {stu3_marks} marks")

# type function
res = print("This is a print statement")
print(res)
print(type(res))

# len function
result = len("Python Programming!!")
print(result)

# list
lst = [1,2,3,4,5]
print(lst)
print(len(lst))

# min function
print(min(10,3,100,40))
print(min(lst))
print(min('A','B','X','M','a'))

# max function
print(max(10,3,100,40))
print(max(lst))
print(max('A','B','X','M','a'))

# round function
print(round(3.1428))
print(round(2.4567777, 2))
print(round(-8.3))

# abs function
print(abs(-3))
print(abs(6))

# sum function
print(sum(lst))

# int function
x=int("100")
print(x)
print(type(x))

# float function
y=3.14
val=float(y)
print(val)
print(type(val))
print(type(y))

# bool function
z=bool(0)
print(z)
z1=bool(120) # Any non-zero value is True
print(z1)

# input function
color = input("Enter your favorite color: ")
print(f"Your favorite color is {color}")

# age type casted in integer while using the input function
age = int(input("Enter your age: "))
print(f"Your age is {age}")

# exercise 1
name = input("Enter your name: ")
print(f"Good Evening {name}")

# execise 2
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result = num1 + num2
print("Sum is: ", result)

# exercise 3
balance = float(input("Enter your current balance: "))
incre_salary = balance + balance*0.1
print(f"Your increased salary is: {incre_salary}")

### String Practice - can be defined in '', "", ''' ''' or """ """
str1 = 'Hi'
str2 = "Umang"
print(str1, str2)

str3 = '''This is practice of multiple line string
We should use triple quotes for this'''
print(str3)

## \n - to be used for new line in string, \t - to be used for tab space in string,
# \ - to be used for escaping the spacing in the string
str4 = "I am learning Python \n and it is very useful for my career \t I am trying to refresh my Python skills"
str5 = 'That happened to be tonight\'s cricket game'
print(str4)
print(str5)

str6 = "I am going to Julie\'s house"
str6_1='I am going to Julie\'s house'
str6_2='''I am going to Julie\'s house'''
print(str6, str6_1, str6_2)

str7 = "She said, she was \"sick\""
str7_1 = 'She said, she was "sick"'
str7_2 = '''She said, she was "sick"'''
print(str7, str7_1, str7_2)