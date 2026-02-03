# 5)შექმენი სია სადაც შეიყვანთ როგორდც დადებით ასევე უარყოფით რიცხვებს,შენი 
# დავალებაა გაიგო სიაშ მყოფი დადებით რიცხვების 
# ჯამი და უარყოფით რიცხვების რაოდენობა

numbers = [10, -5, 7, -2, -8, 20]

positive_sum = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_count += 1

print("დადებითი რიცხვების ჯამი:", positive_sum)
print("უარყოფითი რიცხვების რაოდენობა:", negative_count)
