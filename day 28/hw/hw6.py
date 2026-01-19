# 6) მომხმარებელს შეაყვანინე ასაკი მანამ, სანამ არ შეიყვანს -1. დაბეჭდე რამდენი ადამიანი იყო არასრულწლოვანი, სრულწლოვანი, პენსიონერი. გამოიყენე while loop + if/elif/else


minor = 0
adult = 0
pensioner = 0

while True:
    age = int(input("შეიყვანე ასაკი (-1 გასაჩერებლად): "))
    
    if age == -1:
        break
    
    if age < 18:
        minor += 1
    elif age <= 64:
        adult += 1
    else:
        pensioner += 1

print("არასრულწლოვანი:", minor)
print("სრულწლოვანი:", adult)
print("პენსიონერი:", pensioner)
