

print("1===================")
i = 1
while i < 11: 
    print(str(i) +".dato")
    i = i + 1
print("===================")
for i in range(1,11):
    print(str(i)+".dato")


print("2--------------------")

for i in range (0, 100):
    print(i)
print("-----------------------")
i = 0
while i <100:
    print(i)
    i = i + 1

print("3***********************")
for i in range(50,100):
    print(i)
print("***********************")
i=50
while i<100:
    print(i)
    i = i + 1
print("4++++++++++++++++++++++")
for i in range(100,200,3):
    print(i)
print("++++++++++++++++++++++")
i=100
while i<200:
    print(i)
    i = i + 3

print("5/////////////////////////")
i = 0
while i <21:
    if i % 2==0:
        print(i)
    i = i + 1
print("/////////////////////////")
for i in range (0, 21):
    if i % 2== 0:
        print(i)
print("6----------------")
i = 5
while i <= 20:
    if i % 2 == 0:
        print(i)
    i = i+1
print("----------------")

for i in range(5, 21):
    if i % 2 == 0:
        print(i)
print("7=================")

for i in range (10,201):
    if i % 10 == 0 and i % 15 == 0:
        print(i)
print("=================")
i = 10 
while i <=200:
    if i % 10 ==0 and i % 15==0:
        print(i)
    i = i + 1
print("8>>>>>>>>>>>>>>>>>>>>>")
password = "dato123"  
sheiyvane_paroli = input("შეიყვანე პაროლი: ")

while sheiyvane_paroli != password:
    sheiyvane_paroli = input("არასწორია, სცადე თავიდან: ")
    

print("სწორია გაარტყი")


