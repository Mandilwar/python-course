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