# 4) შექმენი ცარიელი სია. მომხმარებელს შემოაყვანინე რიცხვები, თუ რიცხვი უკვე არსებობს სიაში შეწყვიტე შეყვანა, სხვა შემთხვევაში დაამატე რიცხვები სიაში, ბოლოს დაბეჭდე მთლიანი სია



numbers = []  

while True:
    ricxvi = int(input("შეიყვანე რიცხვი: "))

    if ricxvi in numbers:
        break
    else:
        numbers.append(ricxvi)

print("საბოლოო სია:", numbers)
