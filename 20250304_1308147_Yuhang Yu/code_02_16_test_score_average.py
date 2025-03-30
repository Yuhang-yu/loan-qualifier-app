#get 3 test scores and calculate the total and average with proper message
score_first = float(input("your first score is :"))
score_second = float(input("your second score is :"))
score_third = float(input("your second score is :"))
#total
score_total = score_first + score_second + score_third
#average
score_ave = score_total / 3
print(f'your total score is {score_total:,.2f}, and your average score is {score_ave:,.2f}')
