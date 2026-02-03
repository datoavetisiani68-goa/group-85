# 6)მომხმარებელს შემოატანინე რაიმე სტრინგი,შენი დავალებაა დაითვალო თუ რამდენი ცალი 
# ხმოვანი და რამდენი ცალი თანხმოვანი გვხვდება 
# მის მიერ შემოყვანილ სტრინგში


text = input("შეიყვანე სტრინგი: ").lower()
vowels = "აეიოუaeiou"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("ხმოვნები:", vowel_count)
print("თანხმოვნები:", consonant_count)
