#Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount
#  and program should tell you in which month that expense occurred. 
# If expense is not found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
expense_month= ["January", "Februray", "March","April","May"]


expense=int(input("Enter a expense value: "))

for i in range(len(expense_list)):
    if expense == expense_list[i]:
        print(expense_month[i])
        break
    else:
        if(expense not in expense_list):
            print("Expense not found")
            break
        else:
            continue


#month_list = ["January", "February", "March", "April", "May"]
# expense_list = [2340, 2500, 2100, 3100, 2980]
# e = input("Enter expense amount: ")
# e = int(e)

# month = -1
# for i in range(len(expense_list)):
#     if e == expense_list[i]:
#         month = i
#         break

# if month != -1:
#     print(f'You spent {e} in {month_list[month]}')
# else:
#     print(f'You didn\'t spend {e} in any month')
