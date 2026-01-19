# 8) შექმენი list: animals = ["dog", "cat", "horse", "cow"] მომხმარებელს შეაყვანინე ცხოველის სახელი, თუ არსებობს  დაბეჭდე მისი index-იმ, თუ არა  "Animal not found"


animals = ["dog", "cat", "horse", "cow"]

animal = input("chawere cxoveli: ")

if animal in animals:
    print(animals.index(animal))
else:
    print("cxovelia ar moidzbena")
