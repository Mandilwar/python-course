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
