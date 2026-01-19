# 7) შექმენი list: letters = ["a", "b", "c", "d", "e"] მომხმარებელს შეაყვანინე ინდექსი, pop()-ით წაშალე ამ ინდექსზე მდგომი ელემენტი, დაბეჭდე წაშლილი ელემენტი და list


letters = ["a", "b", "c", "d", "e"]

index = int(input("chawere indeqsi: "))

removed = letters.pop(index)

print("washlili elementi:", removed)
print("ganaxlebuli listi:", letters)
