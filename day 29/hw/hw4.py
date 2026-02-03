# 4)შექმენი სია და შეიყვანე სტრიგნები პატარა ასოებით,შენი დავალებაა შეამოწმო,
# თუ სტრინგი შეიცავს 5 ასოზე მეტს მაშინ ასეთი სიტყვები ჩაამატე ახალ სიაში ოღონდ 
# პირველი ასო ქონდეთ დიდი ,ხოლო თუ სიტყვა შეიცავს 5 
# ასოზე ნაკლებს მაშინ დაამატე ეს ელემენტებიც სიაში ოღონდ ყველა ასო ქონდეთ დიდი




words = ["python", "hi", "programming", "code", "loop"]
new_words = []

for word in words:
    if len(word) > 5:
        new_words.append(word.capitalize())
    else:
        new_words.append(word.upper())

print(new_words)
