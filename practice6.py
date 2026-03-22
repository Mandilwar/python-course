mtuple=tuple()
print(mtuple)

ftuple=(10.3, 11.5, 12.7, 13.9)
print(ftuple)
print(len(ftuple))
print(max(ftuple))
print(min(ftuple))

ntuple=("Umang","Sanjeev","Rakhi")
print(ntuple)

mtuple=("Umang",25,True)
print(mtuple)

# Difference in Lists and Tuple
# Tuples are immutable and Lists are mutable
# No sorting, appending, extending, inserting, removing can be done in the Tuple
nlist=["Umang","Sanjeev","Rakhi"]
print(nlist)
nlist[0] = "Anand"
print(nlist)

print("Umang" in ntuple)
# conversion of tuple to list
nlist1=list(ntuple)
print(nlist1)

# converion of list to tuple
nlist2=tuple(nlist1)
print(nlist2)

# multiple tuples can be combined
ctuple=ntuple + mtuple
print(ctuple)

xtuple=("a","b","v","d","x","g","i","j","k")
print(xtuple)
print("a" in xtuple)
print("x" in xtuple)