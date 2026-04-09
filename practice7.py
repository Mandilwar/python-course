# Sets do not allow duplicates.

mset=set()
print(mset)
name_set = {'Mary', 'John', 'Alice', 'Bob', 'John'}
print(name_set)
mixed_set = {'Mary', 25, True, 25, 'John'}
print(mixed_set)
# Tuples can be allowed in sets but lists cannot be allowed in sets because they are mutable.
mixed_set1 = {'Mary', 25, True, (1, 2, 3), 'John'}
print(mixed_set1)
# Sets are mutable but they are unordered and unindexed.
laptop_set = {'Dell', 'HP', 'Lenovo', 'Apple'}
print(laptop_set)
laptop_set.add('Asus')
print(laptop_set)
laptop_set.discard('HP')
print(laptop_set) # discard does not raise an error if the element is not present in the set
laptop_set.discard('HP')
print(laptop_set)
laptop_set.remove('Lenovo')
print(laptop_set) # remove raises an error if the element is not present in the set
laptop_set.add('Lenovo')
print(laptop_set)
set1 = {"Anita", "Emma"}
set2 = {"Anita", "Emma", "Olivia"}
set3 = {"James", "Liam"}
res1 = set1.union(set2)
print(res1)
res2 = set1.union(set3)
print(res2)
res3 = set2.intersection(set3)
print(res3)
res4 = set1.intersection(set2)
print(res4)
res5 = set1.difference(set2)
print(res5)
res6 = set2.difference(set1)
print(res6)
print({1,2,3}.isdisjoint({4,5,6}))
print({1,2,3}.isdisjoint({3,4,5}))
print({1,2,3}.issubset({1,2,3,4,5}))
print({1,2,3}.issubset({1,2}))
print({1,2,3}.issuperset({1,2}))

# Practice 1
color_set = {"Red", "Green", "Blue", "Yellow"}
color_set.add("Purple")
color_set.add("Orange")
print(color_set)
color_set.add("Green")
print(color_set)
color_set.discard("Yellow")
print(color_set)