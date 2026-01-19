nums = [1, 2, 3, 4, 5, 6,]
#suashi  axali aitemis chamateba



#siidan amovigot bolo indeqsze mdgomi elementi
# nums.pop(2)


# #elementis chamateba im indeqsze romelzec gvinda (tavshi shuashi boloshi)insert(indeqsi, mnishvneloba)


nums.insert(3,12)

# #siidan im elemntis mnishvnelobis amoshla romelic gvsurs ,mnishvvnelobis agdacemit

nums.remove(4)

# #siidan yveal elementis amoshla 

# nums.clear()


# #indexi abrunebs shexvedris indeqs anu im mnishvnelobis indeqs romelsac frchxilebshi gavuwert
print(nums.index(5))


new_list=[2,3,4,5,"nika","gabrieli","aleqsandre"]
user_input=input("shemoiyvanet raime mnishvneloba:")

if user_input in new_list:
     print(new_list.index(user_input))
else:
     print("araris listshi")

