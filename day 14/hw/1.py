i = 0
while i <= 100:
    print(i)
    i += 1


i = 200
while i <= 400:
    if i % 4 == 0 and i % 5 == 0:
        print(i)
    i += 1


num = int(input("შეიყვანე რიცხვი: "))
i = 2
while i <= num:
    print(i)
    i += 1


num = int(input("შეიყვანე რიცხვი: "))
i = num
while i >= 0:
    print(i)
    i -= 1


secret = 17   # შეგიძლიათ შეცვალოთ
guess = None

while guess != secret:
    guess = int(input(" გამოიცანი რიცხვი: "))

print("სწორია!")


numbers = []

while True:
    x = input("შეიყვანე რიცხვი ან 'გამოთვალე საშუალო': ")

    if x == "გამოთვალე საშუალო":
        break
    numbers.append(int(x))

print(sum(numbers) / len(numbers))


for i in range(0, 51):
    print(i)


for i in range(400, 199, -1):
    print(i)


num = int(input("შეიყვანე რიცხვი: "))
for i in range(1, num + 1):
    print(i*i)


num = int(input("შეიყვანე რიცხვი: "))
i = 1
s = 0

while i <= num:
    s += i
    i += 1

print("ჯამი =", s)


num = int(input("შეიყვანე რიცხვი: "))

s = 0
for i in range(1, num + 1):
    s += i

print("ჯამი =", s)
