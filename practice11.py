number = 100
while number < 90:
    print(number)

num = 7
while num<=10:
    print(num)
    num+=1

num=10
sum_num=0
while num<15:
    sum_num+=num
    num+=1
print(sum_num)

invalid_num=True
current_tries=0
max_tries=3
while invalid_num:
    num=int(input("Enter a number between 100 and 300: "))
    current_tries+=1
    if num >=100 and num <=300:
        invalid_num=False
    elif current_tries >= max_tries:
        invalid_num = False
    else:
        print(f'{num} is not a valid number, Please try again')
print(f'{num} is a last retried number',end = " ")


# Practice 1
num=1
while num <= 10:
    print(num,end=" ")
    num+=1

# Practice 2
n=int(input("Enter a number: "))
num=1
total=0
while num<=n:
    total+=num
    num+=1
print(total)

for letter in "Umang Mandilwar":
    if letter == "a":
        break
    print(letter)
print("Outside for loop")

for num in [3,10,34,23,56]:
    print(num)
    if num == 34:
        print("Number %d has been found ",num)
        break

# Practice 3
l=[23,-9,80,100,12]
print(l)
for num in l:
    if num < 0:
        print(f'{num} is a negative number identified')
        break


i = -3
while i<5:
    if i>=2:
        break
    print(i,"is less than 5")
    i+=1

while True:
    n=int(input("Enter a number: "))
    if n%2==0:
        print(n)
    else:
        print(n,"is an identified odd number")
        break
print("Outside while loop")


## Continue
for letter in "Umang Mandilwar".lower():
    if letter in ["a","e","i","o","u"]:
        continue
    print(letter)


for i in range(1,10):
    print("Before continue statement", i)
    if i%3==0:
        continue
    print("After continue statement", i)


pets = ["Labrador","Golden Retriever","Pug","Greyhound","Bulldog","Cocker Spaniel"]
for pet in pets:
    if pet == "Pug":
        continue
    if pet == "Bulldog":
        break
    print(pet)

for i in range(1,11):
    if i == 5:
        continue
    print(i,end=" ")