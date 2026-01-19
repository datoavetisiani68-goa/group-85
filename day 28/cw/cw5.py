# 4) მომხმარებელს შემოაყვანინე ასაკი, თუ ასაკინ < 18-ზე -> "შენ ხარ არასრულწლოვანი", 
# თუ ასაკი 18 და 64 შორისაა -> "შენ ხარ სრულწლოვანი", თუ ასაკი > 65-ზე -> "შენ ხარ პენსიონერი"


age =int(input('chawere shenia saki:'))

if age <=18:
    print("shen xar arasrulwlovani")
elif age >= 18 and age <= 64:
    print("shen xar srulwlovani")
else:
    print("shenx ar pensioneri")