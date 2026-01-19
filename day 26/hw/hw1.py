# 1) შექმენი ცარიელი სია.მომხმარებელმა შეიყვანოს რიცხვები მანამ, სანამ არ დაწერს "stop".
# დაამატე მხოლოდ დადებითი რიცხვები სიაში, უარყოფითი რიცხვები არ დაამატო, ბოლოს დაბეჭდე სია


numbers=[]


while True:
    gacehreba=input("chawere rame ricxvi an ,stop:")

    if gacehreba == "stop":
        break

    num = int(gacehreba)

    if num >2:
        numbers.append(num)

print("saboloo sia;" ,numbers)