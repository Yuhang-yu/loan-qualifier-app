# in this script, you should pay differently by their sales. If the salesman's sales were over the quota than given him different commission based on promotion ratio
# base quota is 5000
base_quota = 5000
# price of 1 unit of sale is 500
unit_price = 500
# regular commission rate is 0.2
regular_rate = 0.2
# promotion commission rate is 0.5
pro_rate = 0.5
# get input from salesman about month's sales.
month_quota = int(input("Please enter the number of units you sold this month: "))
month_sale = month_quota * unit_price
# calculate sale person's total commission payment
if month_quota > base_quota:  
        over_quota = month_quota - base_quota  
        over_sale = over_quota * unit_price 
        regular_commission = base_quota * unit_price * regular_rate
        extra_commission = over_sale * pro_rate
        total_commission = regular_commission + extra_commission
else:
        total_commission = month_sale * regular_rate

print(f'Your total sales amount is {month_sale:,.2f} yuan.')
print(f'Your total commission is {total_commission:,.2f} yuan.')