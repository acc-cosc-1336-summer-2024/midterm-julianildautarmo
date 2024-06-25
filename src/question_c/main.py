#add import

#part 3.3
import question_c

sales = 0


sales = input("\nHow much did you sell, in US dollars, over the last sales period?\n\n")

bonus = question_c.get_bonus_pay(sales)

if(bonus == "\nInvalid Argument"):
    print(bonus)
else:
    print("\nYou sold a total of $", sales, "of merchandise last sales period and as such are entitled to a bonus of $", bonus,"\n")