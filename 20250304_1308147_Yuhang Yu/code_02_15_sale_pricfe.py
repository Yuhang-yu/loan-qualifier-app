#this program gets an item's original price and calculate its sale price, with a 20% discount
#display amount of cut(discount), discounted price.
#set discount
discount = 0.2
#get a original price
original_price = int(input("what is your pirce:"))
#calculate the amount of discount
amount_disc =original_price * discount
#calculate the diacounted price
price_disc = original_price - amount_disc
#display amount of discount and discounted price with message. number should, after 3 digits, and show 2 digits after dicimal points
print(f'what you selected is {original_price:,.2f} yuan.This time you get a {discount:.0%} dicount. it means you have saved {amount_disc:,.2f} yuan. So total you have to pay is {price_disc:,.2f} yuan.')


