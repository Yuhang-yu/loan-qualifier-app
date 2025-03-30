# This script will calculate payroll in different situation
# Set base hour
base_hour = 40
# Overtime multiplier
ot_multiplier = 1.5
# Money per hour
payrate_per_hour = 1000
# Get work hour for this week
hour = int(input('Please enter total hours that you worked this week:'))
# Calculate the payroll if worker work more than base hour multiply hourly payrate
if hour > base_hour:
    overtime_hour = hour - base_hour
    overtime_pay = overtime_hour * payrate_per_hour * ot_multiplier
    total_payment = (base_hour * payrate_per_hour) + overtime_pay
    print(f'You work {overtime_hour} hour more than {base_hour} hour. So you got {ot_multiplier:0.0%} rate for your extra overload. Payment for the overtime was {overtime_pay:,.2f} yuan. Your total payment is {total_payment:,.2f} yuan')
else:
    total_payment = (base_hour * payrate_per_hour)
    print(f"Here your total payment is {total_payment} yuan")


#payment = hour * payrate_per_hour
#ot_payment = (hour - base_hour) * payrate_per_hour * ot_multiplier
#total_payment = payment + ot_payment