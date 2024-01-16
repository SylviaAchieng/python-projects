#dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#accessing items in a dictionary
x=thisdict["model"]
print(x)

#looping thru a dictionary

for y in thisdict:
    print(y)  #prints key names

    print(thisdict[y])  #prints value names