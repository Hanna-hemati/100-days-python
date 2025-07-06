# print("hello"[-4])
# print(type(89_868_864 + 68_867))

# bmi = 63/1.56**2
# print(bmi)
#
# print(int(bmi))
#
# print(round(bmi))
#
# print(round(bmi, 2))

# score= 0
# score+=1
# print(score)
# print("your score is" +str(score))
# is_winning = True
# print(f"your score is = {score} you are winning is {is_winning}")


print("welcome to the calculator")
bill = float(input("what is the total bill?"))
tip = int(input("how much tip do you like to pay?"))
people = int(input("how many people to split the bill?"))
bill_as_percent= tip/100
total_tip_amount = bill * bill_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"your final amount is {final_amount}")
# print(f"each person should pay{float(bill) / int(people) ** int(100)/ int(tip) }")


