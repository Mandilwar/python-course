games_list =["Football", "Basketball", "Tennis", "Cricket"]
print(games_list)
for game in games_list:
    print(game)
print(game) # accesses the last value of the loop
for letter in ['W', 'e', 'l', 'c', 'o', 'm', 'e']:
    print(letter)

cats = ("Persian", "Siamese", "Maine Coon", "Bengal")
for cat in cats:
    print("It's a ",cat)

names_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names_list:
    print(name.upper())
    print(name,": ",len(name))

n = "Google", "Facebook", "Amazon", "Apple", "Microsoft"
for company in n:
    print(company.lower())

mset = {"Python", "Java", "C++", "JavaScript"}
for language in mset:
    print(language)

num = [78, 45, 23, 89, 12, 56, 34]
for number in num:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


# Practice 1:
number = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for num in number:
    sum += num
print("The sum of the numbers from 1 to 10 is:", sum)

animals = [("Dog", "Bark"), ("Cat", "Meow"), ("Cow", "Moo"), ("Sheep", "Baa")] # List of Tuples
for a in animals:
    print(f'The {a[0]} goes "{a[1]}"')

fruit_weights = [("Apple", 150), ("Banana", 120), ("Orange", 130), ("Grapes", 200)] # List of Tuples
for fruit,weight in fruit_weights:
    print("The weight of {} is {} grams".format(fruit, weight))


# To get the index of the items in the function using enumerate function
for i,t in enumerate(fruit_weights):
    print(f'{i} is the Index of {t}')

games_list =["Football", "Basketball", "Tennis", "Cricket"]
for i, game in enumerate(games_list):
    print(f'{i} is the Index of {game}')

price_history = [{"ticker": "AAPL", "close price": 150, "volume": 1000}, {"ticker": "GOOGL", "close price": 2800, "volume": 500}, {"ticker": "AMZN", "close price": 3400, "volume": 800}]
for stock in price_history:
    print(f'{stock["ticker"]} has a close price of {stock["close price"]} and a volume of {stock["volume"]}')
for price_data in price_history:
    if price_data["close price"] > 2000:
        print(price_data)

names = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}, {"name": "David", "age": 28}, {"name": "Eve", "age": 22}]
for person in names:
    if person["age"] > 25:
        print(person)

game_scores = {"Umang": 3, "Bob": 2, "Charlie": 1, "Goli": 4}
print(game_scores.items())
print(game_scores.keys())
print(game_scores.values())

for name in game_scores:
    print(f'{name}: {game_scores[name]}')

# for-else
characters = {"a", "e", "i", "o", "u"}
for c in characters:
    print(c)
else:
    print("No Characters left in the set")

# Sublists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for elements in matrix:
    print(elements)

# Nested for loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for row in matrix:
    for column in row:
        sum += column
print("The sum of the elements in the matrix is:", sum)

# Range function
srange = range(20)
print(srange)
print(list(srange))
print(tuple(srange))
print(dict(enumerate(srange)))

for i in range(5):
    print(i)

for i in range(0,30,3):
    print(i)

for i in range(-15,15,4):
    print(i,end=" ")

for cube in range(1,8):
    print(cube, "cube is ", cube**3)