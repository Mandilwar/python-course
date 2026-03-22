# Lists

mylist=[]
print(mylist)
print(type(mylist))

# other way to create an empty list
mylist1=list()
print(mylist1)

games=["Cricket", "Football", "Hockey", "Tennis"]
print(games)
print(games[0])
print(games[2])
print(games[-1])
print(games[::-1])
print(games[::2])
print(games[1:3])
print(games[-1] == games[3])
games[2] = "Badminton"
print(games)
games.append("Basketball")
print(games)

l1=[10,20,30,40,50]
l2=[1.5,2.4,3.6,4.8,5.6]
l3=[True, False, False, True]
l4=["Umang", "Sanjeev", 25, 54, True]
print(l1)
print(l2)
print(l3)
print(l4)
l1[0]+=100
print(l1)
l1[3]*=3
print(l1)

print(sum(l1))
print(max(l2))
print(min(l2))

print(sum(l1)/len(l1))

# Practice 1
colors=["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink"]
print(colors[3])

# Practice 2
colors1 = ["Red","Green","Blue","Yellow"]
colors1[3]="Magneta"
print(colors1)

# Practice 3
countries = ["India", "Russia", "USA", "Japan", "Australia"]
print(countries[-1])
print(countries[len(countries)-1])

# Practice 4
num=[1,2,3,4,5,6,7,8,9,10]
print(num[:5])

# Practice 5
languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Typescript"]
print(languages[1:4])

point = [5,10,15]
x,y,z=point
print(x,y,z)

# Practice 6
scores = [95,90,92]
maths, science, english = scores
print("Maths Score = ", maths)
print("Science Score = ", science)
print("English Score = ", english)

# Adding a new movie at the end of the list (Append function)
movie_list = ["Inception", "Interstellar", "The Dark Knight", "Memento", "Dunkirk"]
movie_list.append("Tenet")
print(movie_list)

# Adding a new movie at a specific position (Insert function)
movie_list.insert(2,"Harry Potter: The Goblet of Fire")
print(movie_list)

# removes the value from the list (Remove function)
movie_list.remove("Memento")
print(movie_list)

# Adding multiple or single value(s) in the list (Extend function)
movie_list.extend(["X-Men: The Last Stand", "Fantastic 4"])
print(movie_list)

# Getting the index of a value in the list
print(movie_list.index("Dunkirk"))

# Sorting the list using sort function in ascending order
movie_list.sort()
print(movie_list)

# Sorting the list in descending order
movie_list.sort(reverse=True)
print(movie_list)

# Removing the last element from the list (pop function)
movie_list.pop()
print(movie_list)

# using list function and defining the values in tuple and converting it to list
movie_tuple = list(("The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"))
print(movie_tuple)

# Sorting based on the key as per length of the movie name
movie_list.sort(key=len)
print(movie_list)

complete_list = movie_list + movie_tuple
print(complete_list)

# To check if a movie is present in the list or not
print("Inception" in complete_list)
print("Bhagam Bhag" in complete_list)
print("Fantastic 4" not in complete_list)

# Practice 7
car_list = list(("Hyundai","Suzuki","Tata","Mahindra"))
print(car_list)
print("Tesla" in car_list)

# Note - for removing the list of values use clear() function.

# Practice 8
country=["India", "Russia", "USA", "Japan", "Australia"]
print(country)
country.append("China")
print(country)
country.insert(2,"Germany")
print(country)
print("Australia" in country)