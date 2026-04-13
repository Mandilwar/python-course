mdict = {} # dictonary is created using curly braces
print(mdict)
print(type(mdict))

emp_salary = {"Umang": 50000, "Sanjeev": 60000, "Rakhi": 55000, "Umang":70000}
print(emp_salary)

print(emp_salary["Umang"]) # duplicate keys are not allowed in dictionary and the last value will be considered for the duplicate key
# Dictionary is mutable, unordered and indexed.
emp_salary["Sanjeev"] = 100000
print(emp_salary)
emp_salary["Anand"] = 75000
print(emp_salary)

emp_salary["Umang"] *= 1.1 # Keys are case sensitive in dictionary
print(emp_salary)

# to remove a key from dictionary
del emp_salary["Anand"]
print(emp_salary)

# Dictionary with Integer Keys
num_dict = {1: "One", 2: "Two", 3:"Three"}
print(num_dict)

# Dictionary with float keys
float_dict = {1.5: "One Point Five", 2.5: "Two Point Five", 3.5: "Three Point Five"}
print(float_dict)

# Dictionary with Mixed Keys
mixed_dict = {"Name": "Alice", 1: "One", 2.5: "Two Point Five", (1,2):"Tuple Key"}
print(mixed_dict)

emp_salary.pop("Rakhi")
print(emp_salary)

print(list(emp_salary.keys()))
print(list(emp_salary.values()))

emp_salary["Rakhi"] = 55000
print(emp_salary)

print(emp_salary.items())

emp_salary.update({"Anand":90000,"Prashant":90000})
print(emp_salary)

print("Umang" in emp_salary.keys())
print(100000 in emp_salary.values())

mdict = {True:"This is True", 2: "This is 2", 3.5: "This is 3.5", "Key": [1,2,3,4,5]} # List can be values in dictionary but not as keys
print(mdict)
print(mdict["Key"][2])

calories = {}
print(calories)
calories["Burger"] = 500
calories["Fries"] = 200
calories["Shake"] = 150
print(calories)

calories["Burger"] = 550
print(calories)

updated_calories = {"Pizza": 300, "Salad": 100, "Shake":200}
calories.update(updated_calories)
print(calories)

# Practice 1
friends = {"Alice": 25, "Bob": 30, "Charlie": 32}
print(friends)
print(friends["Bob"])
friends["Alice"] = 28
print(friends)

# Practice 2
country_capitals = {"India": "New Delhi", "USA": "Washington D.C.", "France": "Paris"}
print(country_capitals)
country_capitals["Germany"] = "Berlin"
print(country_capitals)
country_capitals.pop("USA")
print(country_capitals)

# Practice 3
student_scores = {"Alice": [85, 90, 92], "Bob": [78, 82, 88], "Charlie": [90, 95, 98]}
print(student_scores)
print(student_scores["Alice"][0])
print(student_scores["Bob"][2])