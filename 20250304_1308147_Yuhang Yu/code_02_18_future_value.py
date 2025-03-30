# get the desired future value
future_value = float(input('enter the amount you want to make:'))
# get the annual interset rate
rate = float(input('enter your interest rate:'))
# get the number of years thet the money will appreciate
years = int(input('enter the year the money will grow:'))
# calculate the amount needed to deposit
present_value = future_value / (1 +  rate)**years
# display the amount needed to deposit
print(f'if you want to make {future_value:,.2f} yuan with annual interest rate as {rate:.0%} in {years} years, you need to deposit today {present_value:,.2f}')