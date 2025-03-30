# get a number of seconds from user. caluculate hours, minutes, and seconds
#print(f'{5//2}') 2
#print(f'{5 % 2}') 1
# enter your seconds:504030303939
# that is 533 hour 42 minute and 32 seconds

total_seconds = int (input("please enter the seconds:"))
#calculate hours
hours = total_seconds // 3600
#calculate remaining minutes
minutes = (total_seconds//60) % 60
#get the remaining seconds
seconds = total_seconds % 60
# display the result
print('here ie the time in hours, minuter, and seconds:')
print('hours:', hours)
print('minute:', minutes)
print('second:', seconds)