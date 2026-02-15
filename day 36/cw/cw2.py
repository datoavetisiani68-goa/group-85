# 2) შექმენი ფუქნცია სახელად numbers რომელიც მიიღებს პარამეტრად რაღაც რიცხვს და 
# დაპრინტავს ეს რიცხვი კენტია თუ ლუწი

def numbers(num):
    if num % 2 == 0:
        return "ricxvi luwia"
    else:
        return "ricxvi kentia"


print(numbers(7))
print(numbers(10))
print(numbers(13))