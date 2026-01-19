# 1) შექმენი list: names = ["nika", "luka", "giorgi"]
#  მომხმარებელს შეაყვანინე: ინდექსი და სახელი, insert()-ის გამოყენებით ჩასვი სახელი 
# მითითებულ ადგილას და დაბეჭდე შედეგი

names = ["nika", "luka", "giorgi"]

index=int(input("chawere indeqsi:"))
name=input("chawere saxeli")
names.insert(index,name)

print(names)