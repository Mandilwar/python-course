if True:
    print("Considered as True")
if False:
    print("Considered as False")

a = 1
if a == 1:
    print("Considered as True")
if a > 1:
    print("a>1 is considered as True")
if a >=1:
    print("a>=1 is considered as True")
    res = a + 10
    print(res)
if a <= 10:
    print("a<=10 is considered as True")
    res = a - 10
print(res)

gross_salary = 60000
tax_rate = 15
if gross_salary >= 50000:
    tax_rate = 30
print("Tax rate is 30%")

grading_score = 92
if grading_score >= 90:
    print("Grade A")

# Practice 1
user_score = int(input("Enter your score: "))
if user_score >= 90:
    print("Grade A")
else:
    print("Grade F")

names = ["Alice", "Bob", "Charlie", "David"]
if "Alice" in names:
    names.insert(1, "Eve")
    print(names)
    print(f'{names[0]} is in the list')
if "Peter" not in names:
    names.append("Peter")
    print(names)
    print("Added Peter")

# Practice 2:
names_list = ["Alice", "Bob", "Charlie", "David"]
user_input = input("Enter a name: ")
if user_input in names_list:
    names_list.remove(user_input)
    print(f"{user_input} has been removed from the list.")
    print(names_list)


emp_salary = {"Raj":80000, "Ankit":75000, "Rakhi":60000, "Sonia":85000}
print(emp_salary)
if "Anand" not in emp_salary:
    emp_salary["Anand"] = 75000
print(emp_salary)

if emp_salary["Raj"] > 70000 and emp_salary["Raj"] < 90000:
    print("Raj's salary is between 70000 and 90000 i.e.", emp_salary["Raj"])
    emp_salary["Raj"] *= 1.1
    print("After 10% increment, Raj's salary is", emp_salary["Raj"])
print(emp_salary)


salary = int(input("Enter the salary: "))
if salary < 50000:
    print("Original Salary ", salary)
    salary *= 1.1
    print("After 10% increment, the salary is", salary)
else:
    print("Original Salary ", salary)
    salary *= 1.07
    print("After 7% increment, the salary is", salary)


num = 50
print("Original Number ", num)
num = num - 20 if num > 20 else num + 20
print("Updated Number ", num)

n = 100 
print("Original Number ", n)
res = n/5 if n < 50 else n * 5
print("Updated Number ", res)

student_score = int(input("Enter the student's score: "))
if student_score >= 90:
    print("Grade A")
elif student_score > 80:
    print("Grade B")
elif student_score > 70:   
    print("Grade C")
elif student_score > 60:
    print("Grade D")
else:
    print("Grade F")


# Practice 3
salary = int(input("Enter the salary: "))
if salary > 0 and salary <= 25000:
    print("Original Salary ", salary)
    salary *= 1.1
    print("After 10% increment, the salary is", salary)
elif salary >= 25000 and salary <= 100000:
    print("Original Salary ", salary)
    salary *= 1.07
    print("After 7% increment, the salary is", salary)
elif salary >= 100000 and salary <= 200000:
    print("Original Salary ", salary)
    salary *= 1.05
    print("After 5% increment, the salary is", salary)
else:
    print("Original Salary ", salary)
    salary *= 1.02
    print("After 2% increment, the salary is", salary)


# Nested If-elif-else
items_ordered = int(input("Enter the number of items ordered: "))
items_inventory = int(input("Enter the number of items in inventory: "))
if items_ordered > items_inventory:
    print("Not enough items in inventory to fulfill the order.")
elif items_ordered <= items_inventory:
    if items_ordered == items_inventory:
        print("You are lucky, we have exactly the number of items you ordered in inventory.")
    else:
        print("Your order has been placed successfully.")
    items_inventory -= items_ordered
    if items_inventory < 2:
        print("Inventory is running low. Only", items_inventory, "items left.")
        print("Time to restock the inventory.")


# Practice 4
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:    
    print(number, "is an odd number.")

# Practice 5
number = int(input("Enter a number: "))
if number >= 0:
    print(number, "is a positive number.")
    if number == 0:
        print(number, "is a zero.")
else:    
    print(number, "is a negative number.")