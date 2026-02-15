# 1) შექმენი ფუნქცია რომელიც მიიღებს რაღაც ტექსტს და დააბრუნებს ტექსტში სიმბოლოების რაოდენობას
# 2) შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და დაითვლის ამ ტექსტში ხმოვნების რაოდენობას
# 3) შექმენი ფუქნცია რომელიც მიიღებს რიცხვების სიას [3, 7, 1, 9] და დააბრუნებს ყველაზე დიდ რიცხვს
# 4) შექმენი ფუნქცია რომელიც მიიღებს სიტყვების სიას და დააბრუნებს მხოლოდ იმ სიტყვებს რომლებიც იწყება დიდი ასოთი
# 5) შექმენი ფუქნცია რომელიც იღებს რიცხვების სიას და აბრუნებს მათ საშუალოს
# 6) შექმენი ფუნქცია რომელიც მიიღებს რიცხვს და დააბრუნებს მის კვადრატს
# 7) შექმენი ფუქნცია რომელიც მომხმარებელს შემოაყვანინებს რაღაც რიცხვს და დააბრუნებს სიტყვას ეს რიცხვი დადებითია უარყოფითია თუ ნულია
# 8) შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და ასევე რაღაც რიცხვს, ტექსტსში ყველა ასოა აქციე დიდად და რიცხვითი მნიშვნელობა გადააქცია სტრინგის ტიპად.
# 9) შექმენი ფუქნცია რომელიც მიიღებს რიცხვების სიას და დააბრუნებს მხოლოდ ლუწ რიცხვებს
# 10) დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა გამოკონსოლდეს "Hello, World".
# 11) დაწერეთ ფუქნცია, სახელად celsiusToFahrenheit, რომელიც პარამეტრად მიიღებს ცელსიუსს და გადაიყვანს ფარენჰეიტში. ფორმულა - (Celsius * 9/5) + 32
# 12) დაწერეთ ფუნქცია სახელად sumDigits, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მისი ციფრების ჯამს.
# 13) დაწერეთ ფუნქცია, სახელად calculateArea, რომელიც არგუმენტად მიიღებს ოთხკუთხედის სიგრესა და სიგანეს და დააბრუნებს მის ფართობს. შედეგი გამოიტანეთ ტერმინალში.
# 14) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ პარამეტრს და დააჯამებს ყველა რიცხვს გარკვეულ შუალედში. მაგალითად შეკრიბავს რიცხვებს 5-დან 100-მდე.

# 1
def count_chars(text):
    print(len(text))


# 2
def count_vowels(text):
    vowels = "aeiouAEIOUაეიოუ"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print(count)


# 3
def max_number(numbers):
    print(max(numbers))

max_number([3, 7, 1, 9])


# 4
def capital_words(words):
    result = []
    for word in words:
        if word[0].isupper():
            result.append(word)
    print(result)


# 5
def average(numbers):
    print(sum(numbers) / len(numbers))


# 6
def square(num):
    print(num ** 2)


# 7
def number_type():
    num = int(input("შეიყვანე რიცხვი: "))
    if num > 0:
        print("დადებითია")
    elif num < 0:
        print("უარყოფითია")
    else:
        print("ნულია")


# 8
def text_and_number(text, num):
    print(text.upper())
    print(str(num))


# 9
def even_numbers(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    print(evens)


# 10
def print_hello(times):
    for _ in range(times):
        print("Hello, World")


# 11
def celsiusToFahrenheit(celsius):
    print((celsius * 9/5) + 32)


# 12
def sumDigits(num):
    total = 0
    for d in str(abs(num)):
        total += int(d)
    print(total)


# 13
def calculateArea(length, width):
    print(length * width)


# 14
def sum_in_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    print(total)

sum_in_range(5, 100)
