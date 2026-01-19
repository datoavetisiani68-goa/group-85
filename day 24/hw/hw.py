# 1)
nums = [1,6,7,8,3,12,56,76,90,345,12,33,55]
print(nums[:5])


# 2)
fruits = ["apple", "banana", "cherry", "date", "fig"]
print(fruits[-3:])


# 3)
letters = ["a","b","c","d","e","f","g","h","i","j"]
print(letters[3:8])


# 4)
colors = ["red", "green", "blue", "yellow"]
print(colors[:])


# 5)
text = "Programming"
print(text[:5])


# 6)
word = "HelloWorld"
print(word[-5:])


# 7)
message = "PythonRocks"
print(message[3:9])   # honRoc


# 8)
phrase = "ArtificialIntelligence"
print(phrase[-12:-4])   # Intellig


# 9)
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])


# 10)
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[-2])


# 11)
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[-3])


# 12)
letters = ["a", "b", "c", "d", "e", "f", "g", "o"]
word = letters[-2] + letters[-1] + letters[-2] + letters[0]
print(word)   # goga


# 13)
text = "ჰიდროელექტროსადგური"

start = int(input("შეიყვანე start (0-19): "))
end = int(input("შეიყვანე end (0-19): "))

print(text[start:end])


# 14)
names = ["Nika", "Giorgi", "Ana", "Luka", "Mari"]

# for ციკლი
for name in names:
    print(name)

print("----")

# while ციკლი
i = 0
while i < len(names):
    print(names[i])
    i += 1
