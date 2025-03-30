# This program calculages sales commissions

#create a variable to control the loop
keep_going = 'y'
#calculate a series of commision
while keep_going == 'y':
    sales = float(input('Enter the amout of sales:'))
    comm_rate = float(input('Enter the commision rate:'))
    commision = sales * comm_rate
    print(f'The commision is ${commision:,.2f}.')
 #get a salesperson's sales and commision
 #calculate the commision
 #display the commision
 #see if the user want to do another one

    keep_going = input('Do you want to calculate another commision (enter y for yes):')