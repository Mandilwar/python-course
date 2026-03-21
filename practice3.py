name = "Umang Mandilwar"
print(name)
name_len = len(name)
print(name_len)
print(name[0])
print(name[1])
print(name[-4])
name1 = name[name_len-1]
print(name1)
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = name
print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
animal = "Dog"
print(animal[0:2])
print(animal[0:len(animal)])
x, y, _ = animal
print(x,y,_) # _ Used to ignore the value of the variable.
print(name[0:5]) # String Slicing
print(name[:5])
print(name[6:]) # name[0:0] -- this will print an empty string
name2="James Bond"
print(name2[0:3])
print(name2[3:7])
print(name2[-4:-2])
print(name2[6:8])
print(name2[-4:])

date_string = "21-Mar-2026"
date_string1 = "21-March-2026"
date_string2 = "21-03-2026"
print(date_string[-4:], date_string1[-4:], date_string2[-4:])
date_string_len=len(date_string)
print(date_string_len)
print(date_string[::-1])
# Reorder date from DD-Mmm-YYYY to YYYY-Mmm-DD
parts = date_string.split('-')
reordered_date = f"{parts[2]}-{parts[1]}-{parts[0]}"
print(reordered_date)
print(date_string[::2]) # Skipping every 2nd character
print(name2[1::2]) # Skipping every 2nd character starting from index 1
print(name2[::-2])

# startswith() function
print(name2.startswith("Jam"))
# endswith() function
print(name2.endswith("Jam"))
print(name2.endswith("d"))
# count() function
print(name.count("a"))
# upper() function
print(name.upper())
print(name[3:].upper())
# lower() function
print(name.lower())
print(name.lower().count("a"))
# replace() function
new_name=name.replace("Umang", "Sanjeev")
print(new_name)
# lstrip() function - removes the leading spaces from left
str1="        I like Mangoes.     "
print("***" + str1 + "$$$")
print("***" + str1.lstrip() + "***")
# rstrip() function - removes the trailing spaces from right
print("***" + str1.rstrip() + "***")
# strip() function - removes the leading and trailing spaces from both sides
print("***" + str1.strip() + "***")

sentence = "Python is a great programming language"
print("Python" in sentence)
print("python" in sentence)
print("python" in sentence.lower())

# split function
words = sentence.split()
print(words)

sentence1 = "Python,is,a,great,programming,language"
print(sentence1.split(','))

# join() function - It is used to join the elements of a list into a single string with a specified separator.
rec=" ".join(words)
print(rec)

rec1="*".join(words)
print(rec1)

# practice 1
user=input("Enter your Name: ")
print(user)
user_len = len(user)
print(user_len)
user_upper=user.upper()
print(user_upper)
user_lower=user.lower()
print(user_lower)

# practice 2
str2=input("Enter your name: ")
str3=input("Enter your age: ")
res_str=f"Hello, {str2}! You are {str3} years old."
print(res_str)
res_str1="Hello, {}! You are {} years old.".format(str2, str3)
print(res_str1)