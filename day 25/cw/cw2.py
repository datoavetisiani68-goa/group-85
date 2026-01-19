# 3) შექმენი list, numbers = [10, 20, 30, 40, 50], მომხმარებელს ჰკითხე ინდექსი და pop()-ით წაშალე შესაბამისი ელემენტი
# დაბეჭდე:
# წაშლილი ელემენტი
# განახლებული list

numbers = [10, 20, 30, 40, 50]

index=int(input("shemoiyvane indeqsi:"))

remove=numbers.pop(index)

print("washlili elementi:", remove)
print("axali list:", numbers)