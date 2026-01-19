# 11) შექმენი ცარიელი list მომხმარებელს შემოაყვანინე რიცხვები მანამ სანამ არ დაწერს "stop", ყველა რიცხვი დაამატე ლისთში append()ის გამოყენებით და საბოლოოდ დაბეჭდე ლისთი


nums = []

while True:
    value = input("sheiyvane ricxvi da'stop': ")

    if value == "stop":
        break

    nums.append(int(value))

print(nums)
